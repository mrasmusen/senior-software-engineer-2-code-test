"""
Class to ingest files of various types.
"""

import boto3
import os
import shutil

from app.ingest.json_ingestor import JsonIngestor

class FileIngestor():
    def __init__(self, config, files):
        self.files = files
        self.config = config
        self.ingestors = []

        self._search_s3()

        self._ingest_files()
                
    
    def merge_files(self):
        data = []
        for i in self.ingestors:
            data += i.data
        return data
                
    def _ingest_files(self):
        for filepath in self.files:
            ingestor_type = self._get_ingestor(filepath)

            if ingestor_type:
                ingestor = ingestor_type(filepath)
                self.ingestors.append(ingestor)
                ingestor.ingest_file()

    def _search_s3(self):
        session = boto3.Session(
            aws_access_key_id=self.config.AWS_ACCESS_KEY,
            aws_secret_access_key=self.config.AWS_SECRET_KEY
        )

        s3 = session.resource('s3')

        bucket = s3.Bucket(self.config.S3_BUCKET_NAME)

        s3_object_names = [f.key for f in bucket.objects.all()]

        if len(s3_object_names) > 0:
            if not os.path.exists(self.config.FILESBASEPATH):
                os.mkdir(self.config.FILESBASEPATH)
            for obj in s3_object_names:
                filepath = os.path.join(self.config.FILESBASEPATH, obj)
                bucket.download_file(obj, filepath)

                # Check for duplicates
                if filepath not in self.files:
                    self.files.append(filepath)
    
    def _get_ingestor(self, filepath):
        if filepath.endswith('.json'):
            return JsonIngestor
        else:
            return None

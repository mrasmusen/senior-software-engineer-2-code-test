"""
Wrapper for other ingestors
"""

import gzip
import shutil
import os

class Unzipper():
    def __init__(self, file):
        self.file = file
        self.ingestor = None
    
    def ingest_file(self):
        from app.ingest.file_ingestor import get_ingestor
        with gzip.open(self.file, 'rb') as fin:
            tempfilename = self.file[:-3]
            with open(tempfilename, 'wb') as fout:
                shutil.copyfileobj(fin, fout)
        
            ingestor_type = get_ingestor(tempfilename)

            if ingestor_type:
                self.ingestor = ingestor_type(tempfilename)
                self.ingestor.ingest_file()
                # os.remove(tempfilename)
        
    @property
    def data(self):
        if self.ingestor:
            return self.ingestor.data
        else:
            return []

            
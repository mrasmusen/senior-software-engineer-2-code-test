"""
For ingesting raw json file.
"""

import json

class JsonIngestor():
    def __init__(self, file):
        self.file = file
    
    def ingest_file(self):
        with open(self.file) as f:
            self.data = json.loads(f.read())
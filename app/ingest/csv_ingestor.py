"""
CSV ingestor
"""
import csv

class CSVIngestor():
    def __init__(self, file):
        self.file = file
    
    def ingest_file(self):
        with open(self.file) as csvfile:
            keys = None
            self.data = []
            for idx, row in enumerate(csv.reader(csvfile, delimiter=',')):
                if idx == 0:
                    keys = [k.lower().strip() for k in row]
                    for idx, key in enumerate(keys):
                        if key == "instock":
                            keys[idx] = "in_stock"
                else: 
                    data = [v.strip() for v in row]
                    obj = dict(zip(keys, data))
                    for val in obj.values():
                        val = val.replace('"', '')
                    obj['in_stock'] = obj['in_stock'].lower().startswith('y')
                    self.data.append(obj)
            
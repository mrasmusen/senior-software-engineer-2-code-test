"""
Datastore class
"""
from app.ingest.file_ingestor import FileIngestor
from config import Config

class Datastore():
    def __init__(self, config):
        ingestor = FileIngestor(config, config.FILES)
        self.data = ingestor.merge_files()
        
    def get_product_by_id(self, id):
        for product in self.data:
            if product['id'] == id:
                return product
        

    def get_cheapest_products(self, number):
        def price(item):
            return float(item['price'])
               
        data = sorted(self.data, key=price)
        
        return data[:number]
        
config = Config()
datastore = Datastore(config)

        
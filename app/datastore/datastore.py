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

        # really really inefficient, TODO: make better
        
        def price(item):
            if floatable(item['price']):
                return float(item['price'])
            else:
                return 0
            

        data = sorted(self.data, key=price)
        
        ret = []
        count = 0
        for item in data:
            if floatable(item['price']):
                ret.append(item)
                count += 1
                if count >= number:
                    break
        return ret
        
def floatable(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
    except TypeError:
        return False

config = Config()
datastore = Datastore(config)

        
"""
Config file
"""
from os import (
    getenv,
    listdir
)
from os.path import (
    isfile,
    join
)

class Config():

    @property
    def FLASK_ENV(self):
        return getenv('FLASK_ENV', 'default')

    @property
    def FILES(self):
        basepath = self.FILESBASEPATH
        files = [join(basepath, f) for f in listdir(basepath) if isfile(join(basepath, f))]
        return files
        
    @property
    def FILESBASEPATH(self):
        return getenv('FILESBASEPATH', 'data')

    @property
    def AWS_ACCESS_KEY(self):
        return getenv('AWS_ACCESS_KEY', 'AKIAXLTWLZBPL3FNHTER')
        
    @property
    def AWS_SECRET_KEY(self):
        return getenv('AWS_SECRET_KEY', None)

    @property
    def S3_BUCKET_NAME(self):
        return getenv('S3_BUCKET_NAME', 'pricesearcher-test')
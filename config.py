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
        basepath = self._FILESBASEPATH
        files = [f for f in listdir(basepath) if isfile(join(basepath, f))]
        return files
        
    @property
    def _FILESBASEPATH(self):
        return getenv('FILESBASEPATH', '.')
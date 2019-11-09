import os

from flask import Flask, Blueprint
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix

from config import Config
from app.resources.products import api as products_namespace
from app.datastore.datastore import Datastore

def create_app():

    config = Config()

    # instantiate app
    app = Flask(__name__)

    # set app config
    app.config['FLASK_ENV'] = config.FLASK_ENV
    
    # Set up main API
    api = Api(
        title='Products API',
        version='0.1',
        description='Test API for Products',
        doc='/swagger'
    )

    api.add_namespace(products_namespace)
    
    api.init_app(app)

    # Proxy fix
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return app

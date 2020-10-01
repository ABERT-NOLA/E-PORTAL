import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/resources'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTO_DEST ='app/static/photos'

  

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
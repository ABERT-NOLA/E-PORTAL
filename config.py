import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/exam'

    
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roba:access@localhost/exam'
    
    DEBUG = True


config_options = {
    'development': DevConfig
}
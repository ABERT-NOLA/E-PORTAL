import os


class Config:
    """
    Parent configuration
    """
    SECRET_KEY = 'schoolvirtual'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class ProdConfig(Config):
    """
    Production configuration
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:alex17176251@localhost/portal'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}

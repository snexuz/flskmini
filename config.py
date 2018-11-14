class Config(object):
    DEBUG = False
    TESTING = False
    # DB setting
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

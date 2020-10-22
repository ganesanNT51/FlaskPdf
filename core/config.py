class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql+mysqldb://root:@127.0.0.1:3306/test_app'
    # DATABASE_URI = 'mysql+mysqldb://root:@127.0.0.1:3306/urbanedg_VRConf'
    UPLOAD_PATH  = 'images'
    UPLOAD_FOLDER = 'pdf'
    UPLOADED_FILES = 'static/files'


class DevelopmentConfig(Config):
    DEBUG = True

class SECRET_KEY(Config):
    SECRET_KEY = '5678906567890543346789976565'

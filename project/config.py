from decouple import config

class Config:
    SECRET_KEY='elfrezee13'

class DevelopmentConfig(Config):
    DEBUG = True
    databasename = "proyect_web_facilito"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:pass@localhost/proyect_web_facilito'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    MAIL_SERVER ='smtp.google.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'frezee13@gmail.com'
    #MAIL_PASSWORD = config(MAIL_PASS)
    MAIL_PASSWORD = '####'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:erika#$18@localhost/proyecto_web_facilito_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEST = True

config = {
        'development': DevelopmentConfig,
        'default': DevelopmentConfig,
        'test': TestConfig
}

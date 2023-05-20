##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = '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'


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

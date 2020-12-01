
import os

class BaseConfig:
    TESTING = False
    DEBUG = False

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_ECHO = True
    
    DEBUG = True
   
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_ECHO = True
    TESTING = True
class ProdConfig(BaseConfig):
     pass

configurations = {
      'dev' : DevConfig,
      'test' : TestConfig,
      'prod' : ProdConfig,
 }
 
 

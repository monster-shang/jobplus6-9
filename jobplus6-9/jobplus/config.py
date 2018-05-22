class BaseConfig(object):
    """配置基类"""
    SECRET_KEY = 'very secret key'

class DevelopmentConfig(BaseConfig):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

class ProductionConfig(BaseConfig):
    """生产环境配置"""
    pass
	
class TestingConfig(BaseConfig):
    """"测试环境设置"""
    pass
	
configs = {
	'development':DevelopmentConfig,
	'production':ProductionConfig,
	'testing':TestingConfig
}
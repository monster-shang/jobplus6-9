class BaseCofig(object):
	'''配置基类'''
	SECRET_KEY = 'very secret key'
	

class DevelopmentConfig(BaseCofig):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS=False

	
	
class ProductionConfig(BaseCofig):
	"""生产环境配置"""
	pass
	
class TestingConfig(BaseCofig):
	""""测试环境设置"""
	pass
	
configs = {
	'development':DevelopmentConfig,
	'production':ProductionConfig,
	'testing':TestingConfig
}
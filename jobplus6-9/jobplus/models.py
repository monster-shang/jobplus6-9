from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash

db = SQLAlchemy()

class Base(db.Model):
	__abstract__ = True
	created_at = db.Column(db.Datetime,default=datetime.utcnow)
	updated_at = db.Column(db.Datetime,default=datetime.utcnow,
		onupdate = datetime.utcnow)

user_job = db.Table(
	'user_job',
	db.Column('user_id',db.Integer,db.ForeignKey('user.id',ondelete="CASCADE")),
	db.Column('job_id',db.Integer,db.ForeignKey('job.id',ondelete='CASCADE'))
	)

class User(Base,UserMixin):
	__tablename__ = 'user'

	ROLE_USER = 10
	ROLE_COMPANY = 20
	ROLE_ADMIN = 30

	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(32),unique = True,index = True,nullable = False)
	eamil = db.Column(db.String(64),unique = True,index = True,nullable = False)
	_password = db.Column('password',db.String(256),nullable= False)
	role = db.Column(db.SmallInteger,default=ROLE_USER)
	collect_jobs = db.relationship('Job',secondary = user_job)
	upload_resume_url = db.Column(db.String(64))

	def __repr__(self):
		return '<User:{}>'.format(self.username)

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self,orig_password):
		self._password = generate_password_hash(orig_password)

	def check_password(self,password):
		return check_password_hash(self,_password,password)

	@property
	def is_admin(self):
		return self.role == self.ROLE_ADMIN

	@property
	def is_company(self):
		return self.role == self.ROLE_COMPANY


class Company(Base):
	__tablename__ = 'company'

	id = db.Column(db.Integer,primary_key = True)
	name = db.Column(db.String(64),nullable=False,index=True,unique=True)
	slug = db.Column(db.String(24),nullable=False,index=True,unique=True)
	logo = db.Column(db.String(64),nullable=False)
	site = db.Column(db.String(64),nullable=False)
	contact = db.Column(db.String(24),nullable=False)
	email = db.Column(db.String(24),nullable=False)
	location = db.Column(db.String(24),nullable=False)
	#描述
	description = db.Column(db.String(100))
	#关于
	about = db.Column(db.String(1024))
	#公司标签
	tags = db.Column(db.String(128))
	#公司技术栈
	stack = db.Column(db.String(128))
	#团队介绍
	team_introduction = db.Column(db.String(256))
	#福利，多个福利用分号隔开，最多10个
	welfares = db.Column(db.String(256))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete = 'SET NULL'))
	user = db.relationship('User',uselist = False,backref = db.backref('company',uselist=False))

	def __repr__(self):
		return '<Company {}>'.formate(self.name)

class Job(Base):
	__tablename__ = 'job'

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(24),nullable=False)
	#工资范围
	salary_low = db.Column(db.Integer,nullable=False)
	salary_high = db.Column(db.Integer,nullable=False)
	location = db.Column(db.String(24))
	#职位标签，多个标签用逗号隔开，最多10个
	tags = db.Column(db.String(128))
	experience_requirement = db.Column(db.String(32))
	degree_requirement = db.Column(db.String(32))
	is_fulltime = db.Column(db.Boolean,default = True)
	#是否在招聘
	is_open = db.Column(db.Boolean,default=True)
	company_id = db.Column(db.Integer,db.ForeignKey('company.id',ondelete='CASCADE'))
	company = db.relationship('Company',uselist= False)
	views_count = db.Column(db.Integer,default=0)

	def __repr__(self):
		return '<Job {}>'.format(self.name)

class Dilivery(Base):
	__tablename__ = 'delivery'
	#等待企业审核
	STATUS_WAITING = 1
	#被拒绝
	STATUS_REJECT = 2
	#被接收，等待通知面试
	STATUS_ACCEPT = 3

	id = db.Column(db.Integer,primary_key=True)
	job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
	status = db.Column(db.SmallInteger,default=STATUS_WAITING)

	response = db.Column(db.String(256))
	



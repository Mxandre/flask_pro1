# 开发时间:2024/4/6 16:56
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
SECRET_KEY="jdsdfjsdf_0817"

HOSTNAME = '127.0.0.1'
DATABASE = 'flask_pro1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '0617'
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI=DB_URI

MAIL_SERVER = "smtp.qq.com"
MAIL_USE_TLS = True
MAIL_PORT = 587
# 你个人的邮箱
MAIL_USERNAME = "2505372177@qq.com"
# 刚刚获取到的授权码填在这里
MAIL_PASSWORD = "zxaoxbzsgsacdjci"
# 你的邮箱名字可以和MAIL_USERNAME一样
MAIL_DEFAULT_SENDER = "2505372177@qq.com"



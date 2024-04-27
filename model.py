# 开发时间:2024/4/6 16:57
from ext import db
from datetime import datetime
class user(db.Model):
    __tablename__="users"
    phone = db.Column(db.String(20),nullable=False)
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(100),nullable=False)
    password=db.Column(db.String(1000),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)
    login_time=db.Column(db.DateTime,default=datetime.now)

class EmailCp(db.Model):
    __tablename__ = "emails"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100),nullable=False)

class Question(db.Model):
    __tablename__="questions"
    usersid=db.Column(db.Integer,db.ForeignKey("users.id"))
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)
    author=db.relationship(user,backref="questions")

class Answer(db.Model):
    __table__name="answers"
    id=db.Column(db.Integer,autoincrement=True,primary_key=True)
    question_id=db.Column(db.Integer,db.ForeignKey("questions.id"))
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    answers=db.relationship(Question,backref=db.backref("answers",order_by=create_time.desc()))
    author=db.relationship(user,backref="answers")


# 开发时间:2024/4/14 16:25
import wtforms
from wtforms.validators import Email,Length,EqualTo,InputRequired
from model import user,EmailCp
from ext import db
from flask import g
class RegisterForm(wtforms.Form):
    phone = wtforms.StringField(validators=[Length(min=11,max=11,message="手机号码格式不正确")])
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    captcha = wtforms.StringField(validators=[Length(min=4,max=4,message="验证码格式错误")])
    name = wtforms.StringField(validators=[Length(min=2,max=20,message="姓名长度2~20")])
    password = wtforms.StringField(validators=[Length(min=2,max=20,message="密码长度2~20")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password",message="密码不一致")])

    def validate_phone(self,field):
        phone = field.data
        is_user = user.query.filter_by(phone=phone).first()
        if is_user :
            raise wtforms.ValidationError(message="该手机已注册")
    def validate_email(self,field):
        emails = field.data
        is_user = user.query.filter_by(email=emails).first()
        if is_user :
            raise wtforms.ValidationError(message="该邮箱已注册")


    def validate_captcha(self,field):
        captchas=field.data
        is_email=self.email.data
        is_captcha=EmailCp.query.filter_by(email=is_email,captcha=captchas).first()
        if not is_captcha:
            raise wtforms.ValidationError(message="邮箱验证码错误")
        else :
            db.session.delete(is_captcha)
            db.commit()

class LoginForm(wtforms.Form):
    phone = wtforms.StringField(validators=[Length(min=11,max=11,message="手机号码格式不正确")])
    password = wtforms.StringField(validators=[Length(min=2,max=20,message="密码长度2~20")])


class QuestionForm(wtforms.Form):
    title=wtforms.StringField(validators=[Length(min=3,max=20,message="格式不对")])
    content = wtforms.StringField(validators=[Length(min=3, message="格式不对")])

class AnswerForm(wtforms.Form):
    content=wtforms.StringField(validators=[Length(min=1,message="最少1个字")])
    question_id=wtforms.IntegerField(validators=[InputRequired(message="要输入一个")])


#自定义验证,格式validate_字段名
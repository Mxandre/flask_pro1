# 开发时间:2024/4/6 16:59
from flask import Blueprint,render_template,request,jsonify,redirect,url_for,session
from ext import mail,db
from model import EmailCp,user
from flask_mail import Message
import string
import random
from .form import RegisterForm,LoginForm #当前目录需加.
from werkzeug.security import generate_password_hash,check_password_hash
bp=Blueprint("auth",__name__,url_prefix="/ans")


@bp.route("/register",methods=["POST","GET"])
def register():
    if request.method == "GET" :
        return render_template("register.html")
    else:

        client=RegisterForm(request.form)
        if client.validate():
            mail=client.email.data
            phone=client.phone.data
            name=client.name.data
            password=client.password.data
            new_user=user(email=mail,phone=phone,name=name,password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.register"))


@bp.route("/captcha",methods=["POST"])
def captcha():
    email = request.args.get("email")
    str=string.digits*4
    captcha=random.sample(str,4)
    captcha="".join(captcha)
    print(captcha)
    message = Message(subject="captcha", recipients=[email], body=captcha)
    mail.send(message)
    email_1 = EmailCp(name="lotus", email="xxx@qq.com", captcha=captcha)
    db.session.add(email_1)
    db.session.commit()
    return jsonify({"message": "success"})


@bp.route("/mail/message")
def message():
    message=Message(subject="莲花的生日",recipients=["2505372177@qq.com"],body="happy birthday lotus")
    mail.send(message)
    return "envoyer successfully"

@bp.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        form=LoginForm(request.form)
        if form.validate():
            password=form.password.data
            users=user.query.filter_by(phone=form.phone.data).first()
            if not users:
                print("there is not users ")
                return redirect(url_for('auth.login'))
            if check_password_hash(users.password,password):
                session['user_id']=users.id
                return redirect(url_for('first.home'))
            else:
                print("password incorrect")
                return redirect(url_for('auth.login'))
        else:
            print("格式不正确")
            return redirect(url_for('auth.login'))

@bp.route("logout")
def logout():
    session.clear()
    return redirect(url_for('auth.login'))





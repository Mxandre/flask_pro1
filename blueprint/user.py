# 开发时间:2024/4/6 16:58
from flask import Blueprint,render_template,request,g,redirect,url_for
from .form import QuestionForm
from model import Question
from ext import db
from .decorator import login_decor

bp=Blueprint("user",__name__,url_prefix="/")
@bp.route("abs")
def abs():
    return "hello"

@bp.route("question",methods=["POST","GET"])
@login_decor
def public_question():
    if request.method =="GET":
        return render_template("question.html")
    else:
        question=QuestionForm(request.form)
        if question.validate():
            title=question.title.data
            content=question.content.data
            question=Question(title=title,content=content,author=g.users)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            print(question.errors)
            return redirect(url_for("user.question"))

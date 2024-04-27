# 开发时间:2024/4/21 16:00
from flask import Blueprint,render_template,request,g,redirect,url_for
from model import Question,Answer
from .form import AnswerForm,QuestionForm
from .decorator import login_decor
from ext import db
bp=Blueprint("first",__name__,url_prefix='/first')
@bp.route('/',methods=["POST","GET"])
def home():
    question=Question.query.order_by(Question.create_time.desc()).all()
    return render_template("index.html",questions=question)

@bp.route('/detail/<question_id>')
def detail(question_id):
    question=Question.query.get(question_id)#获取主键
    return render_template("detail.html",question=question)

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
            return redirect(url_for("first.home"))
        else:
            print(question.errors)
            return redirect(url_for("first.public_question"))

@bp.post('/comment')
@login_decor
def comment():
    answers=AnswerForm(request.form)
    if answers.validate():
        content=answers.content.data
        question_id=answers.question_id.data
        comment=Answer(content=content,question_id=question_id,author_id=g.users.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("first.detail",question_id=question_id))
    else:
        print(answers.errors)
        return redirect(url_for("first.detail",question_id=request.form.get("question_id")))

@bp.get('/search')
def search():
    q=request.args.get("q")
    question=Question.query.filter(Question.title.contains(q)).all()
    return render_template("index.html",questions=question)


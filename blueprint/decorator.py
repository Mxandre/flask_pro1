# 开发时间:2024/4/27 15:11
from functools import wraps
from flask import url_for,redirect,g

def login_decor(func):
    #保留函数信息
    @wraps(func)
    def inner(*args,**kwargs):
        if g.users:
            return func(*args,**kwargs)
        else :
            return redirect(url_for("auth.login"))
    return inner

# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from flask import Flask,session,g
import config
from model import user
from ext import db,mail
from blueprint.question import bp as ansbp
from blueprint.user import bp as userbp
from flask_migrate import Migrate
from blueprint.first import bp as firstbp


app=Flask(__name__,static_folder="static",template_folder="templates")
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate=Migrate(app,db)
app.register_blueprint(ansbp)
app.register_blueprint(userbp)
app.register_blueprint(firstbp)

@app.before_request
def before_request():
    user_id=session.get("user_id")
    if user_id:
        users=user.query.get(user_id)
        setattr(g,"users",users)
    else:
        setattr(g,"users",None)

@app.context_processor
def context_processot():
    return {"users":g.users}

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run(debug=True)


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

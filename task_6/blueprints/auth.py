# auth:授权蓝图
from flask import Blueprint, request,jsonify,redirect,url_for,session
from exts import db
from flask import render_template
from flask_mail import Message
from blueprints.forms import RegisterForm
from models import UserModel
from blueprints.forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash

from exts import mail

# /auth
bp = Blueprint("auth",__name__,url_prefix="/auth") # url_prefix="/auth"表示视图函数前缀要加auth


@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("log-in.html")
        #return render_template("login_now.html",message='欢迎来到登录页面',css_url='/static/css/style.css')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在！")
                return redirect(url_for("auth.register"))
            if check_password_hash(user.password,password):
                # cookie:
                # 1.cookie中不适合存储太多数据
                # 2.cookie一般用来存放登录授权的东西
                # 3.flask中的session是加密后存在cookie中的
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))

# GET:从服务器上获取数据
# POST：将客户端的数据提交给服务器
@bp.route("/register",methods=["GET","POST"])
def register():
    if request.method =='GET':
        return render_template("wei.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证：flask-wtf:wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email,username=username,password=generate_password_hash(password)) # 利用Hash对密码进行加密
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))

# 验证用户提交的邮箱和验证码是否对应且正确
# 表单验证：flask-wtf:wtforms

@bp.route("/Index",methods=["GET","POST"])
def Index():
    if request.method=='GET':
        return render_template("Index.html")
    else:
        return redirect(url_for("auth.login"))


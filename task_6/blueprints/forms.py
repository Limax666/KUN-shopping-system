import wtforms
from wtforms.validators import Email,Length,EqualTo
from models import UserModel

# Forms:主要用来验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])  # message为输入格式错误的返回信息
    #captcha = wtforms.StringField(validators=[Length(min=4,max=4,message="验证码格式错误！")])
    username = wtforms.StringField(validators=[Length(min=3,max=20,message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6,max=20,message="密码格式错误！")])

    # 自定义验证：
    # 1.邮箱是否已经被注册
    def validate_email(self,field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="邮箱已被使用！")

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误！")])

# exts.py:这个文件存在的意义是为了解决循环引用的问题
# 插件、扩展文件放在这里
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
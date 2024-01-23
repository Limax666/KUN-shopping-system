from flask import Flask
import config
from exts import db,mail
from blueprints.auth  import bp as auth_bp
from flask_migrate import Migrate


app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app,db)

# blueprint:用来做模块化，不同类型视图函数放在不同blueprint中
#app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run()

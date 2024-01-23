import json
import wtforms
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pyodbc
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'dsasadaSFasf'
CORS(app)

host = 'localhost'
server = 'LAPTOP-ONAUD1LP'
port = '1433'
user = 'sa'
dbpassword = 'lmx021031lmx'
database = 'ctask6'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=ODBC+Driver+17+for+SQL+Server'.format(user, dbpassword, server, port, database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/TETE',methods=['GET','POST'])
def center():
    if request.method == 'GET':
        return render_template("TETE.html")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # 从请求中获取用户名、密码和登录身份
    username = data.get('username')
    password = data.get('password')
    identity_code = data.get('identity')

    try:
        # 连接到 SQL Server 数据库
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+dbpassword)
        cursor = conn.cursor()
        # 执行登录函数并检查结果
        cursor.execute("SELECT dbo.log_in(?,?,?)", username, password, identity_code)
        # 获取第一个结果集的第一行结果
        result = cursor.fetchone()[0]
        customerId = result
        cursor.close()
        # 如果返回值是 'failed'，表示登录失败
        if result == 'failed':
            response_data = {'success': False, 'message': '用户名或密码错误'}
            response = make_response(jsonify(response_data))
        else:
            response_data = {'success': True, 'message': '登录成功'}
            # 创建响应对象
            response = make_response(jsonify(response_data))
            # 使用 session 设置 cookie
            session['username'] = username
            session['password'] = password
            session['customer_id'] = customerId
    except pyodbc.ProgrammingError as e:
        error_message = str(e)
        print(error_message)
        response_data = {'success': False, 'message': '服务器出错'}
        response = make_response(jsonify(response_data))
    finally:
        conn.close()  # 关闭数据库连接

    # 返回 JSON 格式的响应数据
    return response


if __name__ == '__main__':
    app.run()

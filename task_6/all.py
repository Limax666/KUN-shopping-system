import pymssql
from flask import Flask, make_response, Blueprint
from flask import Flask,render_template,jsonify
import pyodbc
from flask import request
from flask_sqlalchemy import SQLAlchemy
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

host = 'localhost'
server = 'LAPTOP-ONAUD1LP'
port = '1433'
user = 'sa'
password = 'lmx021031lmx'
database = 'ctask6'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)

app = Blueprint("auth",__name__,url_prefix="/auth") # url_prefix="/auth"表示视图函数前缀要加auth


@app.route('/purchase',methods=['GET','POST'])
def purchase():
    if request.method == 'GET':
        return render_template("test.html")
    else:
        # 从请求中获取数据
        data = request.get_json()
        dd_id = data.get('dd_id')
        cp_id = data.get('cp_id')
        amount = data.get('amount')

        # 调用存储过程
        cursor = conn.cursor()
        params = {'@dd_id': dd_id, '@cp_id': cp_id, '@amount': amount}
        cursor.execute("EXEC [dbo].[purchase] @dd_id=?, @cp_id=?, @amount=?", dd_id, cp_id, amount)
        conn.commit()
        cursor.close()

        return 'Purchase completed'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("sign-up.html")
    else:
        # 从请求中获取数据
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # 执行注册逻辑，插入数据库等操作
        cursor = conn.cursor()
        params = {'@username': username, '@email': email, '@password': password}
        cursor.execute("EXEC [dbo].[register_user] @username=?, @email=?, @password=?",
                       username, email, password)
        conn.commit()
        cursor.close()

        return 'Registration completed'

@app.route('/products')
def products():
    # 连接 SQL Server 数据库
    server = 'LAPTOP-ONAUD1LP'
    database = 'ctask6'
    username = 'sa'
    password = 'lmx021031lmx'
    conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    cnxn = pyodbc.connect(conn_string)
    cursor = cnxn.cursor()

    # 查询产品表中的数据
    cursor.execute("SELECT 产品id, 产品名称, 单价, 库存量 FROM 产品")
    rows = cursor.fetchall()

    # 将查询结果转换为 JSON 格式并返回
    result = []
    for row in rows:
        product = {}
        product['id'] = row[0]
        product['name'] = row[1]
        product['price'] = row[2]
        product['inventory'] = row[3]
        result.append(product)
    return jsonify(result)

if __name__ == '__main__':
    app.run()

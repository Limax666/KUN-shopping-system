import pymssql
from flask import Flask, make_response
from flask import Flask,render_template,jsonify
import pyodbc
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/call_up/<int:param1>/<int:param2>/<int:param3>')
# 连接数据库
def call_up(param1,param2,param3):
    try:
        conn = pymssql.connect(host='localhost', server='LAPTOP-ONAUD1LP', port='1433', user='sa',
                               password='lmx021031lmx', database='ctask6',
                               charset='utf8')  # 服务器名字，账户，密码，数据库名,字符编码
        cursor = conn.cursor()

        # 执行存储过程
        cursor.execute("{CALL <purchase>(@dd_id,@cp_id,@amount)}", (param1, param2, param3))

        # 获取结果
        rows = cursor.fetchall()

        # 转化为jSON格式
        result = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

        # 创建响应对象
        response = make_response(jsonify(result))

        response.headers["Content-Type"] = "application/json"
        response.status_code = 200

        # 返回结果
        return response

    except Exception as e:
        print(e)
        # 返回错误信息
        return make_response(jsonify({"error": str(e)}), 500)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run()
import pymssql
from flask import Flask, make_response
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


@app.route('/purchase',methods=['GET','POST'])
def purchase():
    if request.method == 'GET':
        return render_template("text.html")
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

if __name__ == '__main__':
    app.run()



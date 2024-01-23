from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timedelta
from flask_cors import CORS
import pyodbc
app = Flask(__name__)
CORS(app)

host = 'localhost'
server = 'LAPTOP-ONAUD1LP'
port = '1433'
user = 'sa'
password = 'lmx021031lmx'
database = 'ctask6'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=ODBC+Driver+17+for+SQL+Server'.format(user, password, server, port, database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
db = SQLAlchemy(app)

# 定义数据库模型
class 订单(db.Model):
    #订单id = db.Column(db.String(50),primary_key=True)
    订购日期 = db.Column(db.DateTime,default=datetime.now)
    发货日期 = db.Column(db.DateTime,default=datetime.now() + timedelta(hours=48))
    到货日期 = db.Column(db.String(100))
    货款确认日期 = db.Column(db.String(100))
    #货主名称 = db.Column(db.String(50))
    #货主地址 = db.Column(db.String(100))
    #货主城市 = db.Column(db.String(100))
    #货主地区 = db.Column(db.String(100))
    #货主国家 = db.Column(db.String(100))
    #货主邮政编码 = db.Column(db.String(50))

    def __init__(self,dingdou_time,fahuo_time,get_time,check_time):
        self.订购日期 = dingdou_time
        self.发货日期 = fahuo_time
        self.到货日期 = get_time
        self.货款确认日期 = check_time

# 创建数据库表

# 定义路由，接收数据并保存到数据库
@app.route('/order2', methods=['POST'])
def save_customer():
    data = request.get_json()

    订单信息 = 订单(
        dingdou_time=data['订购日期'],
        fahuo_time=data['发货日期'],
        get_time=data['到货日期'],
        check_time=data['货款确认日期']
    )

    db.session.add(订单信息)
    db.session.commit()

    return jsonify({'message': '信息已成功保存到数据库！'})

if __name__ == '__main__':
    app.run()
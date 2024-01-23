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
    #订购日期 = db.Column(db.DateTime,default=datetime.now)
    #发货日期 = db.Column(db.DateTime,default=datetime.now() + timedelta(hours=48))
    #到货日期 = db.Column(db.String(100))
    货主名称 = db.Column(db.String(50))
    货主地址 = db.Column(db.String(100))
    货主城市 = db.Column(db.String(100))
    货主地区 = db.Column(db.String(100))
    货主国家 = db.Column(db.String(100))
    货主邮政编码 = db.Column(db.String(50))

    def __init__(self,company_name,address, city, region, postal_code, country):
        self.货主名称 = company_name
        self.货主地址 = address
        self.货主城市 = city
        self.货主地区 = region
        self.货主邮政编码 = postal_code
        self.货主国家 = country

# 创建数据库表

# 定义路由，接收数据并保存到数据库
@app.route('/order', methods=['POST'])
def save_customer():
    data = request.get_json()

    订单信息 = 订单(
        company_name=data['货主名称'],
        address=data['货主地址'],
        city=data['货主城市'],
        region=data['货主地区'],
        postal_code=data['货主邮政编码'],
        country=data['货主国家']
    )

    db.session.add(订单信息)
    db.session.commit()

    return jsonify({'message': '信息已成功保存到数据库！'})

if __name__ == '__main__':
    app.run()
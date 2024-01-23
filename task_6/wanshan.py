from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
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
class 客户(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    客户id = db.Column(db.String(50),primary_key=True)
    公司名称 = db.Column(db.String(100))
    联系人姓名 = db.Column(db.String(100))
    联系人职务 = db.Column(db.String(100))
    地址 = db.Column(db.String(200))
    城市 = db.Column(db.String(100))
    地区 = db.Column(db.String(100))
    邮政编码 = db.Column(db.String(20))
    国家 = db.Column(db.String(100))
    电话 = db.Column(db.String(50))
    传真 = db.Column(db.String(50))

    def __init__(self, customer_id, company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, fax):
        self.客户id = customer_id
        self.公司名称 = company_name
        self.联系人姓名 = contact_name
        self.联系人职务 = contact_title
        self.地址 = address
        self.城市 = city
        self.地区 = region
        self.邮政编码 = postal_code
        self.国家 = country
        self.电话 = phone
        self.传真 = fax

# 创建数据库表

# 定义路由，接收数据并保存到数据库
@app.route('/filling', methods=['POST'])
def save_customer():
    data = request.get_json()

    客户信息 = 客户(
        customer_id=data['客户id'],
        company_name=data['公司名称'],
        contact_name=data['联系人姓名'],
        contact_title=data['联系人职务'],
        address=data['地址'],
        city=data['城市'],
        region=data['地区'],
        postal_code=data['邮政编码'],
        country=data['国家'],
        phone=data['电话'],
        fax=data['传真']
    )

    db.session.add(客户信息)
    db.session.commit()

    return jsonify({'message': '信息已成功保存到数据库！'})

if __name__ == '__main__':
    app.run()
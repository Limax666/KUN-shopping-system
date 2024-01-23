from flask import Flask, render_template, jsonify
import pyodbc

app = Flask(__name__)

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
    cursor.execute("SELECT * FROM 售卖产品清单")
    rows = cursor.fetchall()

    # 将查询结果转换为 JSON 格式并返回
    result = []
    for row in rows:
        product = {}
        product['产品名称'] = row[0]
        product['单价'] = row[1]
        product['中止'] = row[2]
        product['单位数量'] = row[3]
        result.append(product)
    return jsonify(result)

if __name__ == '__main__':
    app.run()

# 所有的配置写在这里


# 数据库配置信息
host = 'localhost'
server = 'LAPTOP-ONAUD1LP'
port = '1433'
user = 'sa'
password = 'lmx021031lmx'
database = 'ctask6'
DB_URI = f"mssql+pymssql://{user}:{password}@{host}:{port}/{database}?charset=utf8"
SQLALCHEMY_DATABASE_URI = DB_URI
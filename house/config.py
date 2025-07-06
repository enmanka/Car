# config.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)



# 直接连接到虚拟机上的 MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:root@192.168.49.134:3306/ixun?charset=utf8mb4"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

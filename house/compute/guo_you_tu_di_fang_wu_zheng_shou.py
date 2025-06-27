# 全国7大区域房价对比
import os

from compute import MysqlConfig
from pyspark import Row

os.environ["PYSPARK_PYTHON"] = r"D:\JavaRelease\Anaconda3\envs\flaskenv\python.exe"
# 华北地区
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext

# 二手房


df = spark.read.load(
    r"E:\Workspace\Workspace__PY\bigdata\house\stock_original_data\guo_you_tu_di_fang_wu_zheng_shou.CSV",
    format="csv", sep=",", inferSchema="true", header="true", encoding="gbk")


def group(item):
    print(item[1])
    return item[1], 1

df.createGlobalTempView("guo_you_tu_di_fang_wu_zheng_shou")


fang_wu_zheng_shou_df = spark.sql("SELECT area,count(*) as counter FROM global_temp.guo_you_tu_di_fang_wu_zheng_shou group by area")

conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
fang_wu_zheng_shou_df.write.jdbc(MysqlConfig.MYSQL_CONN, 'fang_wu_zheng_shou', 'overwrite', conn_param)
print("执行完毕")

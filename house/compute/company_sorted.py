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

company_rdd = sc.textFile("hdfs://localhost:9000/house/company.txt")


def to_pair(item):
    items = item.split("\t")
    return items[0], float(items[1])


pair_rdd = company_rdd.map(lambda x: to_pair(x)).reduceByKey(
    lambda x, y: x + y).map(lambda x: Row(city=x[0], score=x[1]))
schema_company = spark.createDataFrame(pair_rdd)
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
schema_company.write.jdbc(MysqlConfig.MYSQL_CONN, 'company_sorted', 'overwrite', conn_param)
print("执行完毕")

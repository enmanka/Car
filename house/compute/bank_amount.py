# 全国7大区域房价对比
import os


from pyspark import Row
from pyspark.sql import SparkSession

from house.compute import MysqlConfig

os.environ["PYSPARK_PYTHON"] = r"D:\JavaRelease\Anaconda3\envs\flaskenv\python.exe"
# 华北地区


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext

company_rdd = sc.textFile("hdfs://localhost:9000/house/bank_trend.txt")


def to_pair(item):
    items = item.split("\t")
    company_name = items[0]
    try:
        amount = float(items[1])
    except Exception as e:
        amount = 0

    return company_name, amount


pair_rdd = company_rdd.map(lambda x: to_pair(x)).reduceByKey(
    lambda x, y: x + y).map(lambda x: Row(company_name=x[0], amount=x[1]))
schema_bank = spark.createDataFrame(pair_rdd)
conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
schema_bank.write.jdbc(MysqlConfig.MYSQL_CONN, 'company_amont', 'overwrite', conn_param)
print("执行完毕")

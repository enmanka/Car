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
ershoufang_rdd = sc.textFile("hdfs://localhost:9000/house/ershoufang_price.txt")


def to_pair(item):
    tmp_list = item.split(",")
    # 二手房城市
    ershoufang_city = tmp_list[0]
    return ershoufang_city, 1


pair_rdd = ershoufang_rdd.map(lambda x: to_pair(x)).reduceByKey(lambda x, y: x + y).map(
    lambda x: Row(city=x[0], count=x[1]))
schema_ershoufang = spark.createDataFrame(pair_rdd)

conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
schema_ershoufang.write.jdbc(MysqlConfig.MYSQL_CONN, 'city_count', 'overwrite', conn_param)
print("执行完毕")

# 全国7大区域房价对比
import datetime
import os

from compute import MysqlConfig
from pyspark import Row
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

os.environ["PYSPARK_PYTHON"] = r"D:\JavaRelease\Anaconda3\envs\flaskenv\python.exe"
# 华北地区
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext

# 土地房屋征收
gong_zu_fang_rdd = sc.textFile("hdfs://localhost:9000/house/gong_zu_fang.txt")


def to_pair(item):
    datas = item.split("\t")

    try:
        if datas[0] is not None and len(datas[0]) > 0:
            return datas[0], (1, float(datas[1]))
        else:
            return datas[0], (1, 0)
    except Exception as e:
        print("错误的：", datas[0])
        return datas[0], (1, 0)


pair_rdd = gong_zu_fang_rdd.map(lambda x: to_pair(x)).reduceByKey(
    lambda x, y: (x[0] + y[0], x[1] + y[1])).map(lambda x: (x[0], x[1][0], x[1][1] / x[1][0])).map(
    lambda x: Row(location=x[0], counter=x[1], area=x[2]))
schema_gong_zufang = spark.createDataFrame(pair_rdd)

conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
schema_gong_zufang.write.jdbc(MysqlConfig.MYSQL_CONN, 'gong_zu_fang', 'overwrite', conn_param)
print("执行完毕")

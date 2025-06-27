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
tudixiangmu_rdd = sc.textFile("hdfs://localhost:9000/house/k_fgj_yxs_xm_1.txt")


def to_pair(item):
    datas = item.split("\t")
    year = datas[1].split("-")[0]
    try:
        if datas[0] is not None and len(datas[0])>0:
            return year, float(datas[0])
        else:
            return year, 0
    except Exception as e:
        print("错误的：",datas[0])
        return year, 0


pair_rdd = tudixiangmu_rdd.map(lambda x: to_pair(x)).reduceByKey(
    lambda x, y: x + y).map(lambda x: Row(year=x[0], area=x[1]))
schema_ershoufang = spark.createDataFrame(pair_rdd)


conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
schema_ershoufang.write.jdbc(MysqlConfig.MYSQL_CONN, 'yu_shou_trend', 'overwrite', conn_param)
print("执行完毕")

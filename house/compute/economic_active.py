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


def group(item):
    tmp_list = item.split(",")
    # 二手房城市
    ershoufang_city = tmp_list[0]
    price = tmp_list[3]
    if "-" in tmp_list[3]:
        price = tmp_list[3].split("-")[0]

    return ershoufang_city, (1, int(price))


# 二手房键值对RDD
ershoufang_pair_rdd = ershoufang_rdd.map(lambda x: group(x)).reduceByKey(
    lambda x, y: (x[0] + y[0], x[1] + y[1])).map(
    lambda x: Row(city=x[0], count=x[1][0], price=x[1][1] / x[1][0]))

schema_ershoufang_df = spark.createDataFrame(ershoufang_pair_rdd)
schema_ershoufang_df.createGlobalTempView("zufang_shoufang_price_compare")

last_df = spark.sql(
    "SELECT * FROM global_temp.zufang_shoufang_price_compare order by count,price desc limit 10")

conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
last_df.write.jdbc(MysqlConfig.MYSQL_CONN, 'economic_active', 'overwrite', conn_param)
print("执行完毕")

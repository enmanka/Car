from pyspark.mllib.recommendation import ALS
from pyspark.sql import SparkSession

import os
import shutil

if os.path.exists("recommend"):
    shutil.rmtree("recommend")

os.environ["PYSPARK_PYTHON"] = r"D:\JavaRelease\Anaconda3\envs\flaskenv\python.exe"

spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

# 不上传到hdfs
# df = spark.read.load("data/self_select_stock.csv",
#                      format="csv", sep=",", inferSchema="true", header="false")

# 上传到hdfs
df = spark.read.load("hdfs://localhost:9000/data/self_select_stock.csv",
                     format="csv", sep=",", inferSchema="true", header="false")

newdf = df.withColumnRenamed("_c0", 'id').withColumnRenamed("_c1", 'userid').withColumnRenamed("_c2", 'stockid')
# 注册临时表
newdf.createOrReplaceTempView("self_select_stock")
sql = "SELECT userid,stockid,count(1) as score  from self_select_stock GROUP BY userid,stockid"
group_df = spark.sql(sql)
stock_rdd = group_df.rdd.map(lambda item: (item.userid, item.stockid, item.score))
# 训练模型，各参数含义
# rank :  10,模型中隐藏因子数
# iterations ：10  算法迭代次数
# lambda_ ：0.01  ALS中的正则化参数
model = ALS.trainImplicit(stock_rdd, 10, 10, 0.01)

model.save(sc, "recommend")
print("执行完毕！")

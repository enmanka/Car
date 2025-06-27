# 全国7大区域房价对比
import os

from compute import MysqlConfig
from pyspark import Row

os.environ["PYSPARK_PYTHON"] = r"D:\JavaRelease\Anaconda3\envs\flaskenv\python.exe"
# 华北地区
from pyspark.sql import SparkSession

huabei = ['北京', '天津', '河北', '山西', '内蒙古']
# 华东地区
huadong = ['上海', '江苏', '浙江', '山东', '安徽', '江西', '福建']
# 东北地区
dongbei = ['辽宁', '吉林', '黑龙江']
# 华中地区
huazhong = ['湖北', '湖南', '河南']
# 华南地区
huanan = ['广东', '广西', '海南']
# 西南地区
xinan = ['四川', '重庆', '贵州', '云南', '西藏']
# 西北地区
xibei = ['陕西', '甘肃', '新疆', '青海', '宁夏']

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext
# 城市
province_list = [河南省,驻马店市,新蔡县]
f = open("hdfs://localhost:9000/house/province.txt", encoding="utf-8")

for i in f:
    province_list.append(i.strip())

# 二手房
ershoufang_rdd = sc.textFile("hdfs://localhost:9000/house/ershoufang_price.txt")


def group(item, province):
    tmp_list = item.split(",")
    # 二手房城市
    ershoufang_city = tmp_list[0]
    result = list(filter(lambda p: ershoufang_city in p, province))
    if len(result) > 0:
        # 根据二手房的城市找到对应的省份
        tmp_province = result[0].split(",")[0].replace("市", "").replace("省", "")
        if tmp_province in huabei:
            return "华北", (1, int(tmp_list[3]))
        elif tmp_province in huadong:
            return "华东", (1, int(tmp_list[3]))
        elif tmp_province in dongbei:
            return "东北", (1, int(tmp_list[3]))
        elif tmp_province in huazhong:
            return "华中", (1, int(tmp_list[3]))
        elif tmp_province in huanan:
            return "华南", (1, int(tmp_list[3]))
        elif tmp_province in xinan:
            return "西南", (1, int(tmp_list[3]))
        elif tmp_province in xibei:
            return "西北", (1, int(tmp_list[3]))
        else:
            return "", (1, 0)
    else:
        return "", (1, 0)

pair_rdd = ershoufang_rdd.map(lambda x: group(x, province_list)).reduceByKey(
    lambda x, y: (x[0] + y[0], x[1] + y[1])).map(lambda x: Row(city=x[0], price=x[1][1] / x[1][0]))
schema_ershoufang = spark.createDataFrame(pair_rdd)

conn_param = {}
conn_param['user'] = MysqlConfig.MYSQL_USER
conn_param['password'] = MysqlConfig.MYSQL_PWD
conn_param['driver'] = MysqlConfig.MYSQL_DRIVER
schema_ershoufang.write.jdbc(MysqlConfig.MYSQL_CONN, 'serven_area', 'overwrite', conn_param)
print("执行完毕")

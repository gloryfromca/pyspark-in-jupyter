#!/home/zhanghui/py35/bin/python3
import pyspark 
import random
conf = pyspark.SparkConf()
sc = pyspark.SparkContext(conf=conf)

num_samples = 100000000
def inside(p):     
    x, y = random.random(), random.random()
    return x*x + y*y < 1
count = sc.parallelize(range(0, num_samples)).filter(inside).count()
pi = 4 * count / num_samples
print(pi)

# how to spark-submit a task to master to run
# bin/spark-submit --master spark://192.170.5.172:7077  ~/spark_submit.py

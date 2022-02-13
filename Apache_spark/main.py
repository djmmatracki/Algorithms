import findspark

findspark.init("D:/spark")
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext

wordsList = ['python', 'java', 'ottawa', 'ottawa', "Java"]
wordsRDD = sc.parallelize(wordsList, 4)
print(wordsRDD)
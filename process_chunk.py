from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

BASE_PATH = 'hdfs://localhost:9000/data/chunks'

def getSparkSessionInstance(sparkConf):
    if ('sparkSessionSingletonInstance' not in globals()):
        globals()['sparkSessionSingletonInstance'] = SparkSession \
            .builder \
            .config(conf=sparkConf) \
            .getOrCreate()
    return globals()['sparkSessionSingletonInstance']

def process_chunk(time, rdd):
    print(f"========= {time} =========")
    if rdd.isEmpty():
        return
    spark = getSparkSessionInstance(rdd.context.getConf())
    try:
        df = spark.read.json(rdd)
        df.write.parquet(
            f'{BASE_PATH}/processed',
            mode='append'
        )
    except:
        # TODO: Figure out how to filter out files that don't end with ".json"
        pass


if __name__ == '__main__':
    sc = SparkContext("local[*]", "nearspark")
    ssc = StreamingContext(sc, 1)

    chunk = ssc.textFileStream(f'{BASE_PATH}/tmp')
    chunk.foreachRDD(process_chunk)

    ssc.start()
    ssc.awaitTermination()

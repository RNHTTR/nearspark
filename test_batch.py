import json
import requests
from pyspark.sql import SparkSession
# from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()

url = 'https://rpc.testnet.near.org'
data = {
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "block",
  "params": {
    "finality": "final"
  }
}

headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=json.dumps(data))
text = json.dumps(response.json()['result'])
json_rdd = spark.sparkContext.parallelize([text])
df = spark.read.json(json_rdd)
df.show()

base_path = 'hdfs://localhost:9000/data/chunks'

df.write.parquet(f'{base_path}/processed', 'append')
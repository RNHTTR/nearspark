# nearspark
Playing around with streaming [NEAR rpc data](https://docs.near.org/docs/api/rpc) into parquet storage in hdfs

## Getting Started
### Pre-requisites
1. You'll need to have [Docker](https://docker.com) installed.
2. Clone nearspark: `git clone git@github.com:RNHTTR/nearspark.git`

### Run nearspark
```bash
# If you haven't already, navigate to the nearspark directory
cd nearspark

# Fire up the necessary components
docker-compose up

# Create a topic for processing blocks
docker exec -it nearspark_kafka_1 kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 3 --topic process_blocks

# Start the stream reader
docker exec -it nearspark_spark-worker-1_1 spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 process_blocks.py

# Start pulling NEAR data
docker exec -it block-producer python producer.py
```
Voila!

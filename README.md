# nearspark
Playing around with streaming [NEAR rpc data](https://docs.near.org/docs/api/rpc) into parquet storage in hdfs

## Getting Started
### Pre-requisites
1. You'll need an HDFS-compatible file system. HDFS, S3, GCS, etc. Check out [this guide](https://towardsdatascience.com/installing-hadoop-on-a-mac-ec01c67b003c) to run HDFS locally on a Mac.
2. Create the necessary hdfs folders: `hadoop fs -mkdir /data/blocks/processed`
3. Download and install [Apache Kafka](https://kafka.apache.org/quickstart)
    1. Instead of naming the topic "quickstart-events" given in the example, name the topic "process_blocks"

### Run nearspark
1. If you haven't started Zookeeper & Kafka from the pre-requisites, do so now.
2. In a new terminal window, clone this repository with `git clone git@github.com:RNHTTR/nearspark.git` (assuming you're using SSH)
3. Navigate to the project root directory and install the required dependences `cd nearspark && pip install -r requirements.txt`
4. Navigate to the structured streaming directory with `cd sparkstructuredstreaming`
4. Start reading NEAR RPC data and writing it to the Kafka topic by running `python extract_blocks.py`
5. In another new terminal window, start processing the data with the spark job with `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 process_blocks.py`

Voila!

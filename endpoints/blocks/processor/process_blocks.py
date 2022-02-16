from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import (
    ArrayType,
    BooleanType,
    LongType,
    StringType,
    StructField,
    StructType
)

schema = StructType([
    StructField('author', StringType()),
    StructField('chunks', ArrayType(
        StructType([
            StructField('balance_burnt', StringType()),
            StructField('chunk_hash', StringType()),
            StructField('encoded_length', LongType()),
            StructField('encoded_merkle_root', StringType()),
            StructField('gas_limit', LongType()),
            StructField('gas_used', LongType()),
            StructField('height_created', LongType()),
            StructField('height_included', LongType()),
            StructField('outcome_root', StringType()),
            StructField('outgoing_receipts_root', StringType()),
            StructField('prev_block_hash', StringType()),
            StructField('prev_state_root', StringType()),
            StructField('rent_paid', StringType()),
            StructField('shard_id', LongType()),
            StructField('signature', StringType()),
            StructField('tx_root', StringType()),
            StructField('validator_proposals', ArrayType(StringType())),
            StructField('validator_reward', StringType())
        ])
    )),
    StructField('header', StructType([
        StructField('approvals', ArrayType(StringType())),
        StructField('block_merkle_root', StringType()),
        StructField('block_ordinal', LongType()),
        StructField('challenges_result', StringType()),
        StructField('challenges_root', StringType()),
        StructField('chunk_headers_root', StringType()),
        StructField('chunk_mask', ArrayType(BooleanType())),
        StructField('chunk_receipts_root', StringType()),
        StructField('chunk_tx_root', StringType()),
        StructField('chunks_included', LongType()),
        StructField('epoch_id', StringType()),
        StructField('epoch_sync_data_hash', StringType()),
        StructField('gas_price', StringType()),
        StructField('hash', StringType()),
        StructField('height', LongType()),
        StructField('last_ds_final_block', StringType()),
        StructField('last_final_block', StringType()),
        StructField('latest_protocol_version', LongType()),
        StructField('next_bp_hash', StringType()),
        StructField('next_epoch_id', StringType()),
        StructField('outcome_root', StringType()),
        StructField('prev_hash', StringType()),
        StructField('prev_height', LongType()),
        StructField('prev_state_root', StringType()),
        StructField('random_value', StringType()),
        StructField('rent_paid', StringType()),
        StructField('signature', StringType()),
        StructField('timestamp', LongType()),
        StructField('timestamp_nanosec', StringType()),
        StructField('total_supply', StringType()),
        StructField('validator_proposals', ArrayType(StringType())),
        StructField('validator_reward', StringType())
    ]))
])


if __name__ == '__main__':

    spark = SparkSession.builder.getOrCreate()
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "test_process_blocks4") \
        .load() \
        .select(from_json(col("value").cast("string"), schema).alias("block")) \
        .select(col("block.*"))

    query = df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()
    # df.write.parquet(
    #         f'hdfs://localhost:9000/data/blocks/processed',
    #         mode='append'
    #     )

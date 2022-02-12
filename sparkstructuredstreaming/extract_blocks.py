import json
import os
from time import sleep

import requests
from kafka import KafkaProducer
# from confluent_kafka import SerializingProducer
# from confluent_kafka.serialization import StringSerializer
# from confluent_kafka.schema_registry import SchemaRegistryClient
# from confluent_kafka.schema_registry.json_schema import JSONSerializer

URL = 'https://rpc.testnet.near.org'
HEADERS = {"Content-Type": "application/json"}
DATA = {
    "jsonrpc": "2.0",
    "id": "nearspark",
    "method": "block",
    "params": {
        "finality": "final"
    }
}

# PRODUCER = Producer({'bootstrap.servers': })
# schema_registry_conf = {'url': 'http://127.0.0.1:8081'}
# schema_registry_client = SchemaRegistryClient(schema_registry_conf)

# with open("block-json-schema.json") as f:
#     schema_str = json.dumps(json.load(f))
# json_serializer = JSONSerializer(schema_str, schema_registry_client)

# producer_conf = {'bootstrap.servers': 'localhost:9092',
#                 'key.serializer': StringSerializer('utf_8'),
#                 'value.serializer': json_serializer}
# producer = SerializingProducer(producer_conf)

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"], value_serializer=json_serializer
)


def extract_block():
    """
    TODO
    """
    response = requests.request("POST", URL, headers=HEADERS, data=json.dumps(DATA))
    block = response.json()['result']
    hash = block['header']['hash']
    print(f'hash: {hash}')
    
    # producer.produce(
    #     topic='test_process_blocks3',
    #     key=hash,
    #     value=block
    # )

    producer.send('test_process_blocks4', block)
    sleep(3)

if __name__ == '__main__':
    while True:
        extract_block()

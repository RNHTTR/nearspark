"""
Fetches NEAR block data from NEAR RPC Endpoint and writes to Kafka topic
for consumption

TODO:
    - Parameterize environment URL (testnet vs mainnet)
"""
import json
from time import sleep

import requests
from kafka import KafkaProducer

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

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=["kafka:29092"], value_serializer=json_serializer
)

def extract_block():
    """
    Fetches block data from NEAR RPC Endpoint and writes to Kafka topic
    """
    response = requests.request("POST", URL, headers=HEADERS, data=json.dumps(DATA))
    block = response.json()['result']
    hash = block['header']['hash']
    print(f'hash: {hash}')

    producer.send('process_blocks', block)
    sleep(3)

if __name__ == '__main__':
    while True:
        extract_block()

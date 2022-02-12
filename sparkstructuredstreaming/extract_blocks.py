import json
import os
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

    producer.send('test_process_blocks4', block)
    sleep(3)

if __name__ == '__main__':
    while True:
        extract_block()

import json
import os
from time import sleep

import requests

URL = 'https://rpc.testnet.near.org'
DATA = {
    "jsonrpc": "2.0",
    "id": "nearspark",
    "method": "block",
    "params": {
        "finality": "final"
    }
}
HEADERS = {"Content-Type": "application/json"}
HADOOP_HOME = "/usr/local/cellar/hadoop/3.3.1/libexec/bin"

def extract_chunk():
    response = requests.request("POST", URL, headers=HEADERS, data=json.dumps(DATA))
    chunk = response.json()['result']
    hash = chunk['header']['hash']
    print(f'hash: {hash}')
    with open(f'temp/{hash}.json', 'w') as f:
        json.dump(chunk, f)
    
    os.system(f'{HADOOP_HOME}/hadoop fs -moveFromLocal temp/{hash}.json /data/chunks/tmp/{hash}.json')
    sleep(3)


if __name__ == '__main__':
    while True:
        extract_chunk()

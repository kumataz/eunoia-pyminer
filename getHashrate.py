'''
Author: kumataz
Date: 2023-03-29 09:41:43
LastEditors: kumataz
LastEditTime: 2023-03-31 10:43:34
'''
import requests
import json

# Local miner hashrate
def GetMinerHashrate(rpc_url):
    headers = {"Content-type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_hashrate",
        "params": [],
        "id": 1
    }
    response = requests.post(rpc_url, data=json.dumps(payload), headers=headers)
    hashrate = int(response.json()["result"], 16)
    return hashrate

# The whole network hashrate
def GetNetworkHashrate(web3):
    blockNumer = web3.eth.blockNumber
    blockDiff = web3.eth.getBlock(blockNumer).difficulty
    blocktimeAvg = (web3.eth.getBlock(blockNumer).timestamp - web3.eth.getBlock(blockNumer-100).timestamp) / 100
    netHashrate = blockDiff / blocktimeAvg
    return netHashrate

if __name__=='__main__':
    hashrate = GetMinerHashrate("http://localhost:8548")
    print("Hashrate:", hashrate)

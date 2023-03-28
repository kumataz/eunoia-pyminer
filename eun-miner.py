'''
Author: kumataz
Date: 2023-03-16 16:29:41
LastEditors: kumataz
LastEditTime: 2023-03-28 22:14:11
'''
'''
Author: kumataz
Date: 2023-03-16 16:29:41
LastEditors: kumataz
LastEditTime: 2023-03-28 10:41:07
'''
from web3 import Web3
from hashlib import sha256
from datetime import datetime
import os
import time
# import requests
# import json


# # get local hashrate
rpc_url = "http://127.0.0.1:8548"
# headers = {"Content-type": "application/json"}

# payload = {
#     "jsonrpc": "2.0",
#     "method": "ethash_getHashrate",
#     "params": [],
#     "id": 1
# }

# response = requests.post(rpc_url, data=json.dumps(payload), headers=headers)
# hashrate = int(response.json()["result"], 16)
# print("Local Hashrate:", hashrate)


def log(message):
    print('== {} == {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

web3 = Web3(Web3.HTTPProvider(rpc_url))

def main():
    print("Start the fucking bullshit miner..")
    print("Connected to Web3: ", web3.isConnected())

    myaccount = web3.toChecksumAddress("0xf02f639A528eC5e546DfaE38606e2d0962e1abd3")
    balance = web3.eth.getBalance(myaccount)
    log('Current Wallet Balance: {} EUNC'.format(balance,))
    time.sleep(1)

    # threads = os.cpu_count()
    threads = 20
    plural = "" if threads <= 1 else "s"
    log("Mining with {} worker thread{}.".format(threads, plural))    

    # kill this script
    os.system("killall -9 python > /dev/null 2>&1")
    log("Start Miner.. ".format("Now"))
    

    while True:

        blockNumer = web3.eth.blockNumber
        log('Current BlockNumber: {}'.format(blockNumer))
        # blockNumerBaby = blockNumer - 1

        blockDiff = web3.eth.getBlock(blockNumer).difficulty
        print("blockDiff: %d\n" % blockDiff)

        blockTime = web3.eth.getBlock(blockNumer).timestamp
        blockTime2 = web3.eth.getBlock(blockNumer-100).timestamp
        # print("blockTime1: %d, blockTime2: %d\n" % (blockTime, blockTime2))
        blocktimeAvg = (blockTime - blockTime2) / 100
        print("blocktimeAvg: %d\n" % blocktimeAvg)

        fuckHashrate = blockDiff / blocktimeAvg / 1000000
        print("fuckHashrate: %.2f MH/s\n" % fuckHashrate)

        # miner
        miningStatus = web3.eth.mining
        log("Mining status: {}".format(miningStatus))
        if miningStatus == False:
            print("start miner..")
            web3.geth.miner.start(threads)
        time.sleep(5)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        web3.geth.miner.stop()
        exit(0)
    except Exception as e:
        print(": %s" % e)
        exit(0)
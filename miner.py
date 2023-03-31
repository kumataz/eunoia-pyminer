'''
Author: kumataz
Date: 2023-03-16 16:29:41
LastEditors: kumataz
LastEditTime: 2023-03-31 10:50:57
'''
from web3 import Web3
from hashlib import sha256
from datetime import datetime
import os
import time
import getHashrate

def log(message):
    print('== {} == {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

rpc_url = "http://127.0.0.1:8548"
w3 = Web3(Web3.HTTPProvider(rpc_url))

def main():
    print("Start the Eunoia Miner..")
    print("Connected to MinerNode: ", w3.isConnected())

    minerAddress = w3.toChecksumAddress("0xf02f639A528eC5e546DfaE38606e2d0962e1abd3")
    log('Current Wallet Address: {}'.format(minerAddress))
    minerbalance = w3.eth.getBalance(minerAddress)
    log('Current Wallet Balance: {} EUNC'.format(minerbalance))
    CurrentMinerAddress = w3.eth.coinbase
    log('Current Miner Address: {}\n'.format(CurrentMinerAddress))  
    
    # w3.eth.coinbase = minerAddress
    # if current_miner_address == minerAddress:
    #     print("Miner address set to:", minerAddress)
    # else:
    #     print("Failed to set miner address.")
    time.sleep(1)

    # kill this script
    os.system("killall -9 python > /dev/null 2>&1")
    
    while True:

        # block infos
        blockNumer = w3.eth.blockNumber
        log('Current BlockNumber: {}'.format(blockNumer))
        # blocktimeAvg = (w3.eth.getBlock(blockNumer).timestamp - w3.eth.getBlock(blockNumer-100).timestamp) / 100
        # log("AvgBlocktime: {}".format(blocktimeAvg))

        # miner infos
        miningStatus = w3.eth.mining
        log("Mining status: {}".format(miningStatus))
        if miningStatus == False:
            # threads = os.cpu_count()
            threads = 40
            plural = "" if threads <= 1 else "s"
            log("Start Mining with {} worker thread{}.".format(threads, plural))  
            w3.geth.miner.start(threads)

        # blockDiff = w3.eth.getBlock(blockNumer).difficulty
        # netHashrate_M_hs = blockDiff / blocktimeAvg / 1000000
        netHashrate = getHashrate.GetNetworkHashrate(w3)
        log("The Network Hashrate: {:.2f} MH/s".format(netHashrate / 1000000))

        # Miner Hashrate(MH/s)
        minerHashrate = getHashrate.GetMinerHashrate(rpc_url)
        log("Local Miner Hashrate: {:.2f} MH/S\n".format(minerHashrate / 1000000))

        time.sleep(5)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        w3.geth.miner.stop()
        exit(0)
    except Exception as e:
        print(": %s" % e)
        exit(0)
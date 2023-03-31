#!/usr/bin/env python3

from web3 import Web3
from datetime import datetime
import time
import getHashrate

def log(message):
    print('== {} == {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

rpc_url = "http://127.0.0.1:8548"
miner_address = "0xf02f639A528eC5e546DfaE38606e2d0962e1abd3"
w3 = Web3(Web3.HTTPProvider(rpc_url))

def main():
    print("Start the Miner..\nConnected to MinerNode: ", w3.isConnected())
    
    minerAddress = w3.toChecksumAddress(miner_address)
    log('Your Wallet Address: {}'.format(minerAddress))
    minerbalance = w3.eth.getBalance(minerAddress)
    log('Your Wallet Balance: {} ETH'.format(minerbalance / (10**18)))
    CurrentMinerAddress = w3.eth.coinbase
    log('Current Node-Etherbase: {}\n'.format(CurrentMinerAddress))  
    time.sleep(1)
    
    while True:
        # block infos
        blockNumer = w3.eth.blockNumber
        log('Current BlockNumber: {}'.format(blockNumer))

        # miner infos
        miningStatus = w3.eth.mining
        log("Mining status: {}".format(miningStatus))
        if miningStatus == False:
            # threads = os.cpu_count()
            threads = 40
            plural = "" if threads <= 1 else "s"
            log("Start Mining with {} worker thread{}.".format(threads, plural))  
            w3.geth.miner.start(threads)

        netHashrate = getHashrate.GetNetworkHashrate(w3)
        log("The Network Hashrate: {:.2f} MH/s".format(netHashrate / 1000000))
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
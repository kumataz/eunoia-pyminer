'''
Author: kumataz
Date: 2023-03-16 16:29:41
LastEditors: kumataz
LastEditTime: 2023-03-17 16:55:09
'''
from hashlib import sha256
from web3 import Web3
from datetime import datetime
import os
import time


def log(message):
    print('== {} == {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))


def main():
    print("Start the fucking bullshit tool..")

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    print("Connected to Web3: ", w3.isConnected())

    myaccount = w3.toChecksumAddress("0xf02f639A528eC5e546DfaE38606e2d0962e1abd3")
    balance = w3.eth.getBalance(myaccount)
    print("Your current balance is: ", balance, "ETH.")
    time.sleep(1)

    # threads = os.cpu_count()
    threads = 20
    plural = "" if threads <= 1 else "s"
    log("Mining with {} worker thread{}.".format(threads, plural))
    # kill this script
    os.system("killall -9 python > /dev/null 2>&1")

    log('Connected to Ethereum client: %s'.format(w3.clientVersion))
    log("Start Miner ".format("Now"))

    while True:
        time.sleep(5)
        w3.eth.hashrate
        w3.geth.miner.start(threads)


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCtrl+C, bye!")
        w3.geth.miner.stop()
        exit(0)
    except Exception as e:
        print(": %s" % e)
        exit(0)
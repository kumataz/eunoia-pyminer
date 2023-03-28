'''
Author: kumataz
Date: 2023-03-23 17:53:40
LastEditors: kumataz
LastEditTime: 2023-03-23 17:53:42
'''
eth = create_rpc("ETH")
current_height = int(eth.eth_blockNumber(), 16)
sampleSize = 200
current_block = eth.eth_getBlockByNumber(hex(current_height), False)
pre_height = eth.eth_getBlockByNumber(hex(current_height - sampleSize), False)
current_height_time = int(current_block.get("timestamp"), 16)
pre_height_time = int(pre_height.get("timestamp"), 16)

avg_block_time = (current_height_time - pre_height_time) / sampleSize
print(int(current_block.get("difficulty"), 16) / avg_block_time / 1000000000000)


result: 
177.7550919625694
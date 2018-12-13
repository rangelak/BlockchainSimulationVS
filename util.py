import datetime as date
from blockchain import Block

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, "None", date.datetime.now(), "Genesis Block", "0", "0")

def next_block(miner, last_block, data):
  miner.block_id = last_block.block_id + 1
  miner.timestamp = date.datetime.now()
  miner.data = data
  miner.previous_hash = last_block.hash
  return miner.hash_block()
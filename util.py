import datetime as date
from blockchain import Block
import hashlib as hasher

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  sha = hasher.sha256('a')
  sha.update('0')
  hashed = sha.hexdigest()
  return Block(0, "None", date.datetime.now(), "Genesis Block", "0", hashed)

def next_block(miner, last_block, data):
  miner.block_id = last_block.block_id + 1
  miner.timestamp = date.datetime.now()
  miner.data = data
  miner.previous_hash = last_block.hash
  return miner.hash_block()
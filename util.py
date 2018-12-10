import datetime as date
from blockchain import Block

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  data = "Hey! I'm block " + str(this_index)
  previous_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)
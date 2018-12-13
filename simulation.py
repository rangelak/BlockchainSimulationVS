#!/usr/bin/env python2

"""
This is a simulation for the final project for CS143 VeriSign,
a secure Document signing platform on the Blockchain.

Authors: Rangel Milushev, Mustafa Bal, Kaan Armagan. 
Date: 13th December 2018.
"""

from blockchain import Block
from miner import Miner
from signatory import Signatory
from consensus import consensus, verify
from util import create_genesis_block, next_block

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print "Block #{} has been added to the blockchain!".format(block_to_add.index)
  print "Hash: {}\n".format(block_to_add.hash) 
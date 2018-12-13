#!/usr/bin/env python2
from blockchain import Block
import datetime as date
import hashlib as hasher

class Miner(object):
	def __init__(self, 
			block_id, 
			index, 
			timestamp, 
			data, 
			previous_hash):
		self.block_id = block_id
		self.mid = "miner" + str(index)
    	self.timestamp = timestamp
    	self.data = data
    	self.previous_hash = previous_hash

    def hash_block(self):
    	"""
    	Find a hash to put on the blockchain. 
    	"""
	    sha = hasher.sha256('a')
	    found = 0
	    while found == 0:
	    	self.timestamp = date.datetime.now() 
			sha.update(
				str(self.block_id) +
				str(self.mid) + 
			    str(self.timestamp) + 
			    str(self.data) + 
			    str(self.previous_hash))
			hashed = sha.hexdigest()
			if hashed[:2] == '00':
				# Proof of work. Only add the block if startswith 00
				found += 1
				print("*********************************")
				print("Miner: {}", self.mid)
				print("At time: {}", self.timestamp)
				print("With data: {}", self.data)
				print("And previous hash: {}", self.previous_hash)
				print("Generated block with hash: {}", hashed)
			    print("*********************************")
				return Block(self.block_id, self.mid, self.timestamp, self.data, self.previous_hash, hashed)

	def verify_block(self, block):
		"""
		Verify that a block actually has the correct hash when submitted by a different miner
		"""
		sha = hasher.sha256('a')
		sha.update(
			str(block.block_id) +
			str(block.miner_id) + 
	        str(block.timestamp) + 
	        str(block.data) + 
	        str(block.previous_hash))
	    verify_hashed = sha.hexdigest()
	    if verify_hashed != block.hash:
	    	print("Miner ({}) could not verify the previous generated block.", self.mid)
	    	return False
	    return True


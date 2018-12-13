

class Block(object):
  """
  Defining a block of the blockchain
  """
  def __init__(self, 
        block_id, 
        miner_id, 
        timestamp, 
        data, 
        previous_hash, 
        miner_hash):
    self.block_id = block_id
    self.miner_id = miner_id
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = miner_hash
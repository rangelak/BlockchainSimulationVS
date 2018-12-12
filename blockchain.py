import hashlib as hasher

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    sha = hasher.sha256('a')
    found = 0
    while found == 0: 
      sha.update(str(self.index) + 
               str(self.timestamp) + 
               str(self.data) + 
               str(self.previous_hash))
      hashed = sha.hexdigest()
      if hashed[:5] == '00000':
        found += 1
        return hashed

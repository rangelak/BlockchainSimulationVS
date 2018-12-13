#!/usr/bin/env python2
import hashlib as hasher

class Signatory(object);
	def __init__(self, index, value=False, document):
		self.sid = "sig" + str(index)
		self.value = value
		self.document = document
		self.document_hash = hasher.sha256(document)

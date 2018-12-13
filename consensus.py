#!/usr/bin/env python2

"""
IMPORTS
"""
from miner import Miner
from signatory import Signatory

def verify(miner, signatories, document_hash, is_amendment=False):
	"""
	miner: the current miner verifying the agreement; Miner.py
	signatories: a list of all signatories of the agreement; Signatory.py
	document_hash: the document hash submitted by the first party to have signed
	is_amendment: True if the document is an amendment to an existing document.
	"""
	for signatory in signatories:
		if is_amendment == True and signatory.value != True:
			print("{}: Not all signatories have agreed to this amendment", miner.mid)
			return 0
		elif signatory.value != True:
			print("{}: Not all signatories have agreed to this document", miner.mid)
			return 0
		elif signatory.document_hash != document_hash:
			print("{}: Document hashes do not match.", miner.mid)
			return 0

	return 1

def consensus(miners, signatories, document_hash, is_amendment=False):
	"""
	CHECK FOR 51% CONSENSUS ACROSS MINERS
	**************************************
	miners: a list of miners verifying the agreement; Miner.py
	signatories: a list of all signatories of the agreement; Signatory.py
	document_hash: the document hash submitted by the first party to have signed
	is_amendment: True if the document is an amendment to an existing document.
	"""
	miner_count = len(miners)*(1.0)
	verified_count = 0
	for miner in miners:
		verified_count += verify(miner, signatories, document_hash, is_amendment)
	if float(verified_count)/miner_count > 0.5:
		return True
	return False
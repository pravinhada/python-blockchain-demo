from blockchain.blockchain import Blockchain
import hashlib
import json
import sys


def generate_block_id(blockchain):
    """
    generate the unique block_id for the new blockchain block
    """
    return blockchain.blocks[-1].block_id + 1


def generate_block_hash(block_id=0, nonce=0, prev_hash='', transactions=[]):
    """ 
    generate the block hash from the given data 
        block_id: unique block id for each block in blockchain
        nonce: a non negative integer value to satisfy each hash algo
        prev_hash: previous hash value of the block
        transcations: all the transactions in the given block
    """
    block_data = {
        "block_id": block_id,
        "nonce": nonce,
        "prev_hash": prev_hash,
        "transactions": json.dumps(transactions, default=lambda el: el.__dict__)
    }
    print(block_data)
    return hashlib.sha256(json.dumps(block_data).encode()).hexdigest()

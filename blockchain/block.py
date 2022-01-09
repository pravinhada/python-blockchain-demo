import json
from datetime import datetime

import utils.blockchain_constants as constants


class Block:
    """
    A block represent a data structure that holds:
        block_id: id of this block
        prev_hash: A hash from the previous block
        nonce: only one use of value to hash the given block
        transactions: list of all the transaction
        hash: the hash of the current block which can be calculated from above block_id, prev_hash, nonce and transactions,
        this hash will be the prev_hash in next block in the blockchain
    """

    def __init__(self,
                 block_id,
                 prev_hash,
                 nonce,
                 transactions,
                 block_hash,
                 created_date=datetime.now().strftime(constants.DEFAULT_DATE_FORMAT)
                 ):
        self.block_id = block_id
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.transactions = transactions
        self.block_hash = block_hash
        self.created_date = created_date

    def __repr__(self):
        json_str = {
            "block_id": self.block_id,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce,
            "transactions": [el.__dict__ for el in self.transactions],
            "block_hash": self.block_hash,
            "created_date": self.created_date

        }
        return json.dumps(json_str)


def create_genesis_block():
    return Block(block_id=0, prev_hash='', nonce=0, transactions=[], block_hash='', created_date='07/01/2009, 11:11:11')

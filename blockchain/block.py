import json


class Block:
    """
    A block represent a data structure that holds:
        block_id: id of this block
        prev_hash: A hash from the previous block
        nonce: a only one use of value to hash the given block
        transactions: list of all the transaction
        hash: the hash of the current block which can be calculated from above block_id, prev_hash, nonce and transactions, this hash
            will be the prev_hash in next block in the blockchain
    """

    def __init__(self, block_id, prev_hash, nonce, transactions, hash):
        self.block_id = block_id
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.transactions = transactions
        self.hash = hash

    def __repr__(self):
        json_str = {
            "block_id": self.block_id,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce,
            "transactions": json.dumps(self.transactions, default=lambda el: el.__dict__),
            "hash": self.hash

        }
        return json.dumps(json_str)


def get_genesis_block():
    return Block(block_id=0, prev_hash='', nonce=0, transactions=[], hash='')

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

    def __str__(self):
        return f'[{self.block_id}-{self.nonce}-{self.prev_hash}-{self.hash}-{self.transactions}]'

    def __repr__(self):
        return f'[{self.block_id}-{self.nonce}-{self.prev_hash}-{self.hash}-{self.transactions}]'

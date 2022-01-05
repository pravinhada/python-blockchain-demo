from blockchain.blockchain import Blockchain


def generate_block_id(blockchain):
    """
    generate the unique block_id for the new blockchain block
    """
    return blockchain.blocks[-1].block_id + 1


def generate_block_hash(block_id, nonce, prev_hash, transactions):
    """ 
    generate the block hash from the given data 
        block_id: unique block id for each block in blockchain
        nonce: a non negative integer value to satisfy each hash algo
        prev_hash: previous hash value of the block
        transcations: all the transactions in the given block
    """
    return ''

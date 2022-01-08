from blockchain.block import Block
import hashlib


def generate_block_id(blockchain):
    """
    generate the unique block_id for the new blockchain block
    """
    return blockchain.blocks[-1].block_id + 1


def hash_block(block_id, prev_hash, transactions):
    nonce = 0
    generated_hash = ''
    block_data = ''

    while True:
        block_data = '[{}-{}-{}-{}'.format(block_id,
                                           nonce, prev_hash, transactions)
        generated_hash = hashlib.sha256(
            block_data.encode()).hexdigest()
        if generated_hash.startswith('00'):
            print('hash is generated with complexity of 00 as: {}'.format(
                generated_hash))
            break
        else:
            nonce = nonce + 1

    return Block(block_id=block_id, prev_hash=prev_hash, nonce=nonce, transactions=transactions, hash=generated_hash)

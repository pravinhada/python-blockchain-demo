import hashlib

from blockchain.block import Block


def generate_block_id(blocks):
    """
    generate the unique block_id for the new blockchain block
    """
    return blocks[-1].block_id + 1


def hash_block(block: Block):
    nonce = 0
    generated_hash = ''

    while True:
        block_data = '[{}-{}-{}-{}-{}'.format(block.block_id,
                                              nonce, block.prev_hash, block.transactions, block.created_date)
        generated_hash = hashlib.sha256(
            block_data.encode()).hexdigest()
        if generated_hash.startswith('00'):
            print('hash is generated with complexity of 00 as: {}'.format(
                generated_hash))
            break
        else:
            nonce = nonce + 1

    return Block(
        block_id=block.block_id,
        prev_hash=block.prev_hash,
        nonce=nonce,
        transactions=block.transactions,
        block_hash=generated_hash,
        created_date=block.created_date
    )

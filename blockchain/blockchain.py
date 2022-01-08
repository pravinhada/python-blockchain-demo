from datetime import datetime
import json
from os import error

import utils.blockchain_constants as constants
from utils.block_hash import generate_block_id, hash_block

from blockchain.block import Block, create_genesis_block
from blockchain.transaction import Transaction


class Blockchain:
    """
    Blockchain represent the chain of blocks containing transaction and the block hash
    """

    def __init__(self, blocks=[], open_transactions=[]):
        self.blocks = blocks
        self.open_transactions = open_transactions

    def __repr__(self):
        json_str = {
            "blocks": json.dumps(self.blocks, default=lambda el: el.__dict__),
            "open_transactions": json.dumps(self.open_transactions, default=lambda el: el.__dict__)
        }
        return json.dumps(json_str)


def read_block(block):
    """ read the json block to the block object """
    mapped_transactions = block['transactions']
    transactions = []
    for tnx in mapped_transactions:
        transactions.append(read_transaction(tnx))
    return Block(block['block_id'], block['prev_hash'],
                 block['nonce'], transactions, block['hash'], block['created_date'])


def read_transaction(transaction):
    """ read the json transaction to the transaction object """
    return Transaction(transaction['sender'], transaction['receiver'], float(transaction['amount']), created_date=transaction['created_date'])


def read_blockchain_file(file_name):
    """ read the blockchain from the given file as file_name, the first line of file is blockchain and second line is
    open_transactions """
    blockchain = None
    import os

    # check if file is empty
    if os.stat(file_name).st_size == 0:
        return None

    try:
        with open(file_name, mode='r') as f:
            loaded_blocks = json.loads(f.readline())
            loaded_transactions = json.loads(f.readline())

            blocks = []
            open_transactions = []

            for chain in loaded_blocks:
                block = read_block(chain)
                blocks.append(block)

            for tnx in loaded_transactions:
                transaction = read_transaction(tnx)
                open_transactions.append(transaction)

            blockchain = Blockchain(blocks, open_transactions)

    except Exception as e:
        print('Error while reading blockchain file: ', e)

    return blockchain


def read_blockchains():
    """ Returns all the blockchain, if stored in file, retrieve it otherwise return genesis block for now """
    blockchain = read_blockchain_file('data/blockchain.txt')
    if blockchain is None:
        # create the file here
        genesis_block = hash_block(create_genesis_block())
        add_genesis_block(genesis_block)
        return [genesis_block], []
    else:
        return blockchain.blocks, blockchain.open_transactions


def add_genesis_block(genesis_block):
    """ add new genesis block and empty open transactions to the file """
    blocks = [genesis_block]
    open_transactions = []
    try:
        with open('data/blockchain.txt', mode='w') as f:
            f.write(str(blocks).replace("'", '"'))
            f.write('\n')
            f.write(str(open_transactions).replace("'", '"'))
    except Exception as e:
        print('Failed to write genesis block to file', e)


def add_open_transaction(transaction=[]):
    """ add new transactions to the open transactions list """
    blocks, open_transactions = read_blockchains()
    open_transactions.append(transaction)
    try:
        with open('data/blockchain.txt', mode='w') as f:
            f.write(str(blocks).replace("'", '"'))
            f.write('\n')
            f.write(str(open_transactions).replace("'", '"'))
    except error:
        print('error updating blockchain data, try again!' + error)


def save_blockchain(blocks, open_transactions):
    """ save both blockchain and open transaction to the file """
    try:
        with open('data/blockchain.txt', mode='w') as f:
            f.write(str(blocks))
            f.write('\n')
            f.write(str(open_transactions))
    except error:
        print('error while saving the mined blockchain' + error)


def mine_new_block():
    """ 
    mine the new block and add this to the blockchain
        1: get all the open transactions
        2: read previous blockchain
        3: read new block id
        4: create new hash for newily mined block
        5: update the blockchain file and add new block to chain
    """
    blockchain = read_blockchain_file('data/blockchain.txt')
    new_block_id = generate_block_id(blockchain)
    prev_hash = blockchain.blocks[-1].hash
    open_transactions = blockchain.open_transactions[:]

    # adding reward transaction too
    open_transactions.append(Transaction(
        sender=constants.DEFAULT_SENDER, receiver=constants.DEFAULT_RECEIVER, amount=constants.DEFAULT_REWARD))

    block_to_hash = Block(
        block_id=new_block_id,
        prev_hash=prev_hash,
        nonce=0,
        transactions=open_transactions,
        hash='',
        created_date=datetime.now().strftime(constants.DEFAULT_DATE_FORMAT)
    )
    hashed_block = hash_block(block_to_hash)
    new_blocks = blockchain.blocks.copy()
    new_blocks.append(hashed_block)
    save_blockchain(new_blocks, [])

import json
import os
from datetime import datetime
from pathlib import Path
import functools

import utils.blockchain_constants as constants
from blockchain.block import Block, create_genesis_block
from blockchain.transaction import Transaction
from utils.block_hash import generate_block_id, hash_block

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE = os.path.join(DATA_DIR, 'blockchain.txt')


class Blockchain:
    """
    Blockchain represent the chain of blocks containing transaction and the block hash
    """

    def __init__(self, blocks=[], open_transactions=[]):
        self.blocks = blocks
        self.open_transactions = open_transactions
        self.__read_blockchain_file(DATA_FILE)
        self.__balance = 0

    def __repr__(self):
        json_str = {
            "blocks": json.dumps(self.blocks, default=lambda el: el.__dict__),
            "open_transactions": json.dumps(self.open_transactions, default=lambda el: el.__dict__)
        }
        return json.dumps(json_str)

    @staticmethod
    def read_transaction(transaction):
        """ read the json transaction to the transaction object """
        return Transaction(transaction['sender'], transaction['receiver'], float(transaction['amount']),
                           created_date=transaction['created_date'])

    @staticmethod
    def read_block(block):
        """ read the json block to the block object """
        mapped_transactions = block['transactions']
        transactions = []
        for tnx in mapped_transactions:
            transactions.append(Blockchain.read_transaction(tnx))
        return Block(block['block_id'], block['prev_hash'],
                     block['nonce'], transactions, block['block_hash'], block['created_date'])

    def __read_blockchain_file(self, file_name):
        """ Private method: read the blockchain from the given file as file_name, the first line of file is blockchain and second line is
        open_transactions """
        try:
            # check if file is empty
            if os.stat(file_name).st_size == 0:
                return None

            with open(file_name, mode='r') as f:
                loaded_blocks = json.loads(f.readline())
                loaded_transactions = json.loads(f.readline())

                blocks = []
                open_transactions = []

                for chain in loaded_blocks:
                    block = Blockchain.read_block(chain)
                    blocks.append(block)

                for tnx in loaded_transactions:
                    transaction = Blockchain.read_transaction(tnx)
                    open_transactions.append(transaction)

                self.blocks = blocks
                self.open_transactions = open_transactions

        except Exception as e:
            print('Error while reading blockchain file: ', e)

    def read_blockchains(self):
        """ Returns all the blockchain, if stored in file, retrieve it otherwise return genesis block for now """
        if self.blocks is None or len(self.blocks) == 0:
            self.__add_genesis_block()

        return self.blocks

    def read_open_transactions(self):
        """ Return all the open transactions that are yet to be mined """
        return self.open_transactions

    def __add_genesis_block(self):
        """ add new genesis block and empty open transactions to the file """
        self.blocks = [hash_block(create_genesis_block())]
        self.open_transactions = []
        self.save_blockchain()

    def add_new_transaction(self, transaction=None):
        """ add new transactions to the open transactions list """
        self.open_transactions.append(transaction)
        self.save_blockchain()

    def save_blockchain(self):
        """ save both blockchain and open transaction to the file """
        try:
            with open(DATA_FILE, mode='w') as f:
                f.write(str(self.blocks).replace("'", '"'))
                f.write('\n')
                f.write(str(self.open_transactions).replace("'", '"'))
        except IOError as e:
            print('Error while saving the blockchain and transactions to file: ' + e)
            return False

        return True

    def mine_new_block(self):
        """
        mine the new block and add this to the blockchain
            1: get all the open transactions
            2: read previous blockchain
            3: read new block id
            4: create new hash for newly mined block
            5: update the blockchain file and add new block to chain
        """
        if len(self.open_transactions) == 0:
            print('There are no open transactions to mine new bitcoins')
            return

        new_block_id = generate_block_id(self.blocks)
        prev_hash = self.blocks[-1].block_hash
        open_transactions = self.open_transactions[:]

        # adding reward transaction too
        open_transactions.append(Transaction.get_reward_transaction())

        block_to_hash = Block(
            block_id=new_block_id,
            prev_hash=prev_hash,
            nonce=0,
            transactions=open_transactions,
            block_hash='',
            created_date=datetime.now().strftime(constants.DEFAULT_DATE_FORMAT)
        )
        hashed_block = hash_block(block_to_hash)
        self.blocks.append(hashed_block)
        self.open_transactions = []
        is_success = self.save_blockchain()
        if is_success:
            print('Blockchain mine is successful, Congratulation, you got 6.25 bitcoins')
        else:
            print('Better luck mining next time')

    def get_balance(self):
        all_transactions = []
        received = 0.0
        sent = 0.0
        for block in self.blocks:
            for tx in block.transactions[:]:
                all_transactions.append(tx)

        amount_received = [float(tx.amount)
                           for tx in all_transactions if tx.receiver == 'XXX']
        if len(amount_received) > 0:
            received = functools.reduce(lambda a, b: a + b, amount_received)

        amount_sent = [float(tx.amount)
                       for tx in all_transactions if tx.sender == 'XXX']

        if len(amount_sent) > 0:
            sent = functools.reduce(lambda a, b: a+b, amount_sent)

        self.__balance = received - sent
        print('Total balance: {}'.format(self.__balance))
        return self.__balance

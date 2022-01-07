import json
from os import O_EXCL, error

from blockchain.block import Block, get_genesis_block


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


def read_blockchains():
    """ Returns all the blockchain, if stored in file, retrieve it otherwise return genesis block for now """
    try:
        with open('data/blockchain.txt', mode='r') as f:
            # first line blockchain
            chain = json.loads(f.readline())
            # second line open transaction
            open_transactions = json.loads(f.readline())
            return (chain, open_transactions)
    except:
        print('file not found, returning genesis block')
        return (get_genesis_block(), [])


def add_open_transaction(transaction=[]):
    """ add new transactions to the open transactions list """
    blockchain, open_transactions = read_blockchains()
    open_transactions.append(transaction)
    try:
        with open('data/blockchain.txt', mode='w') as f:
            f.write(str(blockchain).replace("'", '"'))
            f.write('\n')
            f.write(str(open_transactions).replace("'", '"'))
    except error:
        print('error updating blockchain data, try again!' + error)

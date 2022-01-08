import unittest
import json

from utils.block_hash import generate_block_id, hash_block
from blockchain.block import Block
from blockchain.blockchain import Blockchain, read_blockchain_file
from blockchain.transaction import Transaction


class BlockHashTest(unittest.TestCase):

    blocks = []
    open_transactions = []
    blockchain = None

    def setUp(self):
        self.blockchain = read_blockchain_file('data/blockchain.txt')
        self.blocks = self.blockchain.blocks
        self.open_transactions = self.blockchain.open_transactions

    def tearDown(self):
        self.blocks.clear()
        self.open_transactions.clear()

    def test_block_not_none(self):
        self.assertIsNotNone(self.blocks)
        self.assertIsNotNone(self.open_transactions)

    def test_generate_block_id(self):
        block_id = generate_block_id(self.blockchain)
        print(f'New block id is: {block_id}')
        self.assertIsNotNone(block_id)

    def test_hash_block(self):
        block_id = generate_block_id(self.blockchain)
        prev_hash = self.blocks[-1].hash
        hashed_block = hash_block(
            block_id=block_id, prev_hash=prev_hash, transactions=self.open_transactions)
        print(hashed_block)

if __name__ == '__main__':
    unittest.main()

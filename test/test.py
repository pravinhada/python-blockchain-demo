from blockchain.transaction import Transaction
from blockchain.block import Block
from blockchain.blockchain import Blockchain
from utils.block_hash import generate_block_id

tx1 = Transaction(sender='prabin', reciever='jdoe', amount=1.0)
tx2 = Transaction(sender='prabin', reciever='pete', amount=1.2)

transactions = [tx1, tx2]

block1 = Block(0, '', 0, transactions, '')
block2 = Block(1, '', 0, [Transaction(
    sender='Jonny', reciever='Matt', amount=2.5)], '')

blockchain = Blockchain([block1, block2], [])

print(blockchain)
print(generate_block_id(blockchain))

from blockchain.transaction import Transaction
from blockchain.block import Block
from blockchain.blockchain import Blockchain
from utils.block_hash import generate_block_id, hash_block

tx1 = Transaction(sender='paul', reciever='jdoe', amount=1.0)
tx2 = Transaction(sender='peter', reciever='pete', amount=1.2)

transactions = [tx1, tx2]

block1 = Block(0, '', 0, transactions, '')
block2 = Block(1, '', 0, [Transaction(
    sender='jonny', reciever='matt', amount=2.5)], '')

blockchain = Blockchain([block1, block2], [])

print(transactions)
print(block1)
print(blockchain)
print(generate_block_id(blockchain))

print(hash_block(block_id=1, prev_hash='cb5fe943b6508eebda1233375620ba05afdf9ac567a4eb4ab46d83f3904886fd',transactions=transactions))
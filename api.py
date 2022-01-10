from flask import Flask, jsonify, request

from blockchain.blockchain import Blockchain
from blockchain.transaction import Transaction

# initialize blockchain here
blockchain = Blockchain()


def get_blockchain():
    """ return all the blocks in the blockchain [GET]/api/blockchain """
    blocks = blockchain.read_blockchains()
    chains = [block.__dict__.copy() for block in blocks]
    for chain in chains:
        chain['transactions'] = [tx.__dict__ for tx in chain['transactions']]
    return jsonify(chains), 200


def create_transaction():
    """ create new bitcoin transaction, need sender, receiver and amount [POST]/api/transaction """
    try:
        data = request.json
        sender = data['sender']
        receiver = data['receiver']
        amount = int(data['amount'])
        transaction = Transaction(
            sender=sender, receiver=receiver, amount=amount)
        blockchain.add_new_transaction(transaction=transaction)
    except Exception as e:
        print('Exception occurred while creating new transaction: ', e)
        err_msg = {
            'status': 400,
            'message': 'Error occurred while creating new transaction, please check your input data'
        }
        return jsonify(err_msg), 400

    return 'successful', 200


def get_open_transactions():
    """ return all open transactions before the block is created [GET]/api/transaction """
    open_transactions = blockchain.read_open_transactions()
    return jsonify([obj.__dict__ for obj in open_transactions]), 200


def mine():
    """ mine the new block and add to the blockchain list/file [POST]/api/mine """
    blockchain.mine_new_block()
    return jsonify({
        'message': 'Mining bitcoin is successful',
        'status': 200
    }), 200

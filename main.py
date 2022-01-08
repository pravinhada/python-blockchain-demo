from flask import Flask, render_template, request, jsonify
import json

from blockchain.blockchain import read_blockchains, add_open_transaction, mine_new_block
from blockchain.transaction import Transaction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ just a index page """
    return render_template('hello.html')


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    """ return all the blocks in the blockchain """
    blocks, _ = read_blockchains()
    # return jsonify([block.__dict__ for block in blocks])
    return json.dumps(blocks, default=lambda b: b.__dict__, indent=4)


@app.route('/create_transaction', methods=['POST'])
def create_transaction():
    """ create new bitcoin transaction, need sender, receiver and amount """
    data = request.json
    sender = data['sender']
    receiver = data['receiver']
    amount = int(data['amount'])
    transaction = Transaction(sender=sender, receiver=receiver, amount=amount)
    add_open_transaction(transaction=transaction)
    return 'successful'


@app.route('/open_transactions', methods=['GET'])
def get_open_transactions():
    """ return all open transactions before the block is created """
    _, open_transactions = read_blockchains()
    return jsonify([obj.__dict__ for obj in open_transactions])


@app.route('/mine', methods=['GET'])
def mine_block():
    """ mine the new block and add to the blockchain list/file """
    mine_new_block()
    return 'successful'


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5001
    print(f'Server is running at {host}:{port}')
    app.run(host=host, port=port)

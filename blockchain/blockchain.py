import json


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

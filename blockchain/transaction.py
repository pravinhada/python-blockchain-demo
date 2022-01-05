from datetime import datetime
import json


class Transaction:
    """
    A transaction class containing sender, receiver and amount data
    """

    def __init__(self, sender, reciever, amount=0.0):
        self.sender = sender
        self.receiver = reciever
        self.amount = amount
        self.date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def __repr__(self):
        return json.dumps(self.__dict__)

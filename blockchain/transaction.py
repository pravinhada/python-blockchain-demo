from datetime import datetime
import json


class Transaction:
    """
    A transaction class containing sender, receiver and amount data
    """

    def __init__(self, sender, receiver, amount=0.0, date=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        if date is None:
            self.date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        else:
            self.date = date

    def __repr__(self):
        return str(self.__dict__)

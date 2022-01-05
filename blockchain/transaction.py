from datetime import datetime

class Transaction:
    """
    A transaction class containing sender, receiver and amount data
    """

    def __init__(self, sender, reciever, amount=0.0):
        self.sender = sender
        self.receiver = reciever
        self.amount = amount
        self.date = datetime.now()

    def __str__(self):
        return f'({self.sender} sent {self.receiver} {self.amount} bitcoins on {self.date.strftime("%m/%d/%Y, %H:%M:%S")})'

    def __repr__(self):
        return f'({self.sender} sent {self.receiver} {self.amount} bitcoins on {self.date.strftime("%m/%d/%Y, %H:%M:%S")})'

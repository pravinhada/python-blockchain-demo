from datetime import datetime

import utils.blockchain_constants as constants


class Transaction:
    """
    A transaction class containing sender, receiver and amount data
    """

    def __init__(self, sender, receiver, amount=0.0, created_date=datetime.now().strftime(constants.DEFAULT_DATE_FORMAT)):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.created_date = created_date

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def get_reward_transaction():
        """ 
        This is static method, returns the reward transaction for the user who mine the bitcoin.
        At this moment the bitcoin mine reward is 6.25 defined in DEFAULT_REWARD
        """
        return Transaction(sender=constants.DEFAULT_SENDER, receiver=constants.DEFAULT_RECEIVER, amount=constants.DEFAULT_REWARD)

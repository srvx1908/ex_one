import atm_machine
class account:

    def __init__(self,owner,balance=0):

        self.owner= owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    deposit()
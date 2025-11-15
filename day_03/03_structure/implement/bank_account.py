class OverWithdrawError(ValueError):
    pass

class NegativeDeposit(ValueError):
    pass
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDeposit('Deposit amount cannot be negative')
        if amount < 100:
            raise ValueError('Minimum deposit amount is 100')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise OverWithdrawError('Insufficient Balance')
        
        self.balance -= amount

    def print_balance(self):
        print(self._balance)




# try:
bank_account = BankAccount()
bank_account.deposit(-1)
bank_account.withdraw(10)
# except ValueError as e:
#     print('Error encountered')
#     print(e)

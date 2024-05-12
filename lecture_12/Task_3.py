class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        self._balance = balance

account = BankAccount(5455321532148798, 1000)
print("Номер рахунку:", account.get_account_number())
print("Баланс:", account.get_balance())

account.set_balance(1500.0)
print("Оновленний баланс:", account.get_balance())

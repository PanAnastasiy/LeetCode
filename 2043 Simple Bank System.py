class Bank:

    def __init__(self, balance: list[int]):
        self.accounts = {i: balance[i - 1] for i in range(1, len(balance) + 1)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.accounts or account2 not in self.accounts:
            return False
        if self.accounts[account1] >= money:
            self.accounts[account1] -= money
            self.accounts[account2] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.accounts:
            self.accounts[account] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.accounts:
            return False
        if self.accounts[account] >= money:
            self.accounts[account] -= money
            return True
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
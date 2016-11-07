class BankAccount():

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self. currency = currency
        self.history_strings = [""]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history_strings.append(
                "Deposited amount of" + str(amount) + self.currency)
        else:
            raise ValueError("Amount is incorrect for this operation!")
            self.history_strings.append(
                "Failed to deposit amount of" + str(amount) + self.currency)

    def balance(self):
        self.history_strings.append(
            "Balance check ->" + str(self.balance) + self.currency)
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history_strings.append(
                "Withdrawal for" + str(amount) + self.currency)
            return True
        else:
            self.history_strings.append(
                "Failed to withdraw" + str(amount) + self.currency)
            return False

    def __str__(self):
        return "Bank account for {0} with balance of {1}{2}".format(
            self.name, self.balance, self.currency)

    def __int__(self):
        return self.balance

    def transfer_to(self, account, amount):
        if amount <= self.balance:
            self.balance -= amount
            account.balance += amount
            self.history_strings.append(
                "Transfered" + str(amount) + self.currency +
                "to account" + account.name)
            return True
        else:
            self.history_strings.append(
                "Failed to transfer" + str(amount) +
                self.currency + "to account" + account.name)
            return False

    def history(self):
        return self.history_strings


def main():
    account = BankAccount("Rado", 0, "$")
    account2 = BankAccount("Ivo", 0, "$")

    account.deposit(1000)
    account.withdraw(500)
    account.transfer_to(account2, 200)
    print(account.history())


main()

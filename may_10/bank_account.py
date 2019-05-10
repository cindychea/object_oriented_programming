class BankAccount:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def __str__(self):
        return "Your balance is ${} and you are earning an interest rate of {}%.".format(self.balance, self.interest_rate)

    def deposit_money(self, dep_amount):
        self.balance += dep_amount
        return "You just made a deposit! Your new balance is ${:.2f}.".format(self.balance)

    def withdraw_money(self, with_amount):
        self.balance -= with_amount
        return "You just made a withdrawal! Your new balance is ${:.2f}.".format(self.balance)

    def gain_interest(self):
        self.balance = self.balance + self.balance * self.interest_rate
        return "You just earned interest! Your new balance is ${:.2f}.".format(self.balance)

saving_acc = BankAccount(2000, 0.3)
print(saving_acc)
print(saving_acc.deposit_money(500))
print(saving_acc.withdraw_money(250))
print(saving_acc.gain_interest())
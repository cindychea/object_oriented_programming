import math

class Paperboy:

    def __init__(self, name, experience, earnings):
        self.name = name 
        self.experience = experience
        self.earnings = earnings
        self.quota_num = 0 

    def find_quota(self):
        return math.ceil(self.experience / 2 + 50) 

    def __str__(self):
        return "My name is {}. Time to start delivering papers!".format(self.name)

    def quota(self):
        return "The quota for {}'s next delivery is {}.".format(self.name, self.find_quota())

    def deliver(self, start_address, end_address):
        quota_num = self.find_quota() 
        papers_delivered = abs(end_address - start_address)
        self.experience += papers_delivered
        over_quota = papers_delivered - quota_num
        if over_quota > 0:
            money_earned = over_quota * 0.50 + quota_num * 0.25
        else:
            money_earned = papers_delivered * 0.25
        if papers_delivered < quota_num:
            money_earned -= 2
        self.earnings += money_earned 
        return "{:.2f}".format(money_earned)

    def report(self):
        return "I'm {}, I've delivered {} papers and I've earned {} so far!".format(self.name, self.experience, self.earnings)

pb1 = Paperboy('Josh', 123, 100)
pb2 = Paperboy('Fabio', 0, 100)
print(pb1)
print(pb2)
print(pb1.quota())
print(pb2.quota())
print(pb1.deliver(100, 25))
print(pb2.deliver(100, 75))
print(pb1.report())
print(pb2.report())
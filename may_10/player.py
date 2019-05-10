class Player:

    def __init__(self, gold_coins = 0, health_points = 10, lives = 5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives
    
    def __str__(self):
        return "Welcome, player! You have {} lives left.".format(self.lives)

    def level_up(self):
        self.lives += 1
        return "You just levelled up! You now have {} lives.".format(self.lives)

    def collect_treasure(self):
        self.gold_coins +=1
        if self.gold_coins % 10 == 0:
            self.level_up()
        return "You collected treasure! You now have {} gold coins.".format(self.gold_coins)

    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1 
            self.health_points = 10
            if self.lives <= 0:
                self.restart()
        return "You were damaged in battle! You have {} lives and {} health points.".format(self.lives, self.health_points)

    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

player1 = Player()
player2 = Player(9, 20, 1)
# print(player1)
# print(player2)
# print(player1.level_up())
# print(player2.level_up())
# print(player1.collect_treasure())
# print(player2.collect_treasure())
print(player1.do_battle(11))
print(player2.do_battle(20))


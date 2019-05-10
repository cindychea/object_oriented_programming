class Cat:

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time
    
    def __str__(self):
        return "{} has his meal at {}:00 h and likes to eat {}.".format(self.name, self.meal_time, self.preferred_food)
    
    def eats_at(self):
        if self.meal_time <= 11:
            return "{} eats at {} AM.".format(self.name, self.meal_time)
        elif self.meal_time <= 23:
            self.meal_time = self.meal_time - 12
            return "{} eats at {} PM.".format(self.name, self.meal_time)
        else:
            return "{} does not seem to have a valid meal time.".format(self.name)

    def meow(self):
        return "Meow! My name is {} and I eat {} at {}:00 h! PLEASE FEED ME OR ELSE.".format(self.name, self.preferred_food, self.meal_time)

cat1 = Cat('Nemo', 'tuna', 7)
cat2 = Cat('Lenny', 'salmon', 23)
cat3 = Cat('Roger', 'kale', 25)

print(cat1)
print(cat1.eats_at())
print(cat1.meow())
print(cat2)
print(cat2.eats_at())
print(cat2.meow())
print(cat3)
print(cat3.eats_at())
print(cat3.meow())

# Is there a way to get the result from eats_at function and put it in meow function?
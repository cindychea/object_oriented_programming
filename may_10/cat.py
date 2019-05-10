class Cat:

    def __init__(self, name, preferred_food, meal_time):
        self.name = name
        self.preferred_food = preferred_food
        self.meal_time = meal_time
    
    def __str__(self):
        return "{} has his meal at {}:00 h and likes to eat {}.".format(self.name, self.meal_time, self.preferred_food)
    
    def eats_at(self):
        if self.meal_time >= 24:
            return None
        elif 23 <= self.meal_time >= 12:
            self.meal_time = abs(self.meal_time - 12)
            return "{} PM".format(self.meal_time)
        else:
            return "{} AM".format(self.meal_time)

    def meow(self):
        return "Meow! My name is {} and I eat {} at {}! PLEASE FEED ME OR ELSE.".format(self.name, self.preferred_food, self.eats_at())

cat1 = Cat('Nemo', 'tuna', 7)
cat2 = Cat('Lenny', 'salmon', 23)
cat3 = Cat('Roger', 'kale', 25)

# print(cat1)
# print(cat1.eats_at())
print(cat1.meow())
# print(cat2)
# print(cat2.eats_at())
print(cat2.meow())
# print(cat3)
# print(cat3.eats_at())
print(cat3.meow())

# MEOW seems to be calling the function again and the time is not right????
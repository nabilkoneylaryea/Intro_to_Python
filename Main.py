# Classes and objects


class SuperHero:

    team = 'Avengers' # default team

    #special type of function called initializer like a constructor in java to set up valuees
    def __init__(self, name, health):
        self.name = name
        self.health = health

    #method
    def take_damage(self, amount):
        self.health -= amount

thor = SuperHero('thor', 100)
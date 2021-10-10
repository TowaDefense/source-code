

class Player:

    
    maxHp = 100

    def _init_(self):
        self.health = None
        self.name = None
        self.character = None

    def _init_(self, health, name, character):
        self.health = health
        self.name = name
        self.character = character


    def setMaxHP (self, max):
        self.maxHP = max
    
    def heal (self, regen):
        if (self.health + regen > self.maxHP):
            self.health = self.maxHP
        else:
            self. health += regen
    

    
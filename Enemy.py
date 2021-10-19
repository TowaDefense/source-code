from cocos import *

class Enemy:
    
    def _init_(self):
        self.name = None
        self.tier = None
        self.MaxHealth = None
        self.health = None
        self.sprite = None
        self.speed = None
        self.special = None
    
    def takeDamage(self, dmg: int):
        self.hp -= dmg

    

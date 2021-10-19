from cocos import *

class Tower :


    def _init_(self):
        self.name = None
        self.type = None
        self.weapon = None
        self.upgrades = []
        self.sprite = None
    def _init_(self, name: str, type: bool, weapon: Weapon, upgrades: [], spriteFileName: str):
        self.name = name
        self.type = type
        self.weapon = Weapon
        self.upgrades = upgrades
        self.sprite = cocos.sprite.Sprite(spriteFileName)
   
    def seeUpgrades(self):
        return self.upgrades

    

    
            

    

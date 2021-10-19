
class entity:
    
    def _init_(self, name: str, maxHP: int):
        self.name = name
        self.maxHP = maxHP
        self.health = maxHP
    
    def getName(self):
        return self.name

    def getMaxHP(self):
        return self.maxHP

    def getHP(self): 
        return self.health
    





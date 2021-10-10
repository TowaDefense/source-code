
from skillTree import skillTree

class Hero:



    def _init_(self):
        self.name = None
        self.weapon = None
        self.description = None
        self.skills = skillTree() 
        self.activeSkills = []
        self.activeBranch = None
    
    def getSkills (self):
        self.activeSkills = self.skills.getAllEffects(self.activeBranch)
    
    
    
    #def applyEffects(self):
    
    



    

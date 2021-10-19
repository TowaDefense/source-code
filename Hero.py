
from skillTree import skillTree



class Hero (Tower):



    def _init_(self):
        super ()
        self.description = None
        self.skills = skillTree() 
        self.activeSkills = []
        self.activeBranch = 0

    
    def getSkills (self):
    
        self.activeSkills = self.skills.getAllEffects(self.activeBranch)

    def setSprite (self, fileName: str):
        self.appearance
    
    def setActiveSkillBranch(self, path: int):
        self.activeBranch = path
    


    
    
    
    #def applyEffects(self):
    
    


  



class effect:
    class Modifier:
        
        #Todo Figure out how we want modifiers to work

        def _init (self):
            self.type = None
            self.modifier = None
        
        #def getType():
        #    return self.type
        
        #def getModifier():
        #    return self.modifier
               

    active = bool(False)


    def _init_(self):
        self.description = None
        self.modifier = None


    
    def _init_(self, description: str, modifier: Modifier, isActive: bool):
        self.description = description
        self.modifier = modifier
        self.active = isActive

        
    def getDescription(self):
        return self.description

    def getModifierType (self):
        return self.modifierType
    

    #def setModifierType (self, ModifierType):
    #    self.setModifierType = modifierType

    #def setModifier(self, modifier):
    #    self.modifier = modifier
    
    def isActive(self):
        return self.active
    
    def setStatus(self, status: bool):
        self.active = status
    
    def changeStatus(self):
        self.active = not self.active
    


    



from effect import effect

class branch:

    def _init_(self):
        self.name = None
        self.effect = effect()
        self.left = None
        self.right = None
        self.middle = None

    def _init_ (self, name, effect: effect):
        self.name = name
        self.effect = effect



    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def getMiddle(self):
        return self.middle

    def getEffect(self):
        return self.effect
    
    def getName(self):
        return self.name
    
    def setEffect(self, description: str, type: str, modifier):
        self.effect.setDescription(description)
        self.effect.setModifierType(type)
        self.effect.setModifier(modifier)
    
    def setLeft (self, branch):
        self.left = branch
    
    def setRight (self, branch):
        self.right = branch
    
    def setMid (self, branch):
        self.middle = branch

    

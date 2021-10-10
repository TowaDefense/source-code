from effect import effect

class branch:

    def _init_(self):
        self.name = None
        self.effect = effect()
        self.left = None
        self.right = None
        self.middle = None

    def _init_ (self, name, effect):
        self.name = name
        self.effect = effect

    def getLeft():
        return self.left
    
    def getRight():
        return self.right

    def getMiddle():
        return self.middle

    def getEffect():
        return this.effect
    
    def getName():
        return self.name
    
    def setEffect(self, description, type, modifier):
        self.effect.setDescription(description)
        self.effect.setModifierType(type)
        self.effect.setModifier(modifier)
    
    def setLeft (self, branch):
        self.left = branch
    
    def setRight (self, branch):
        self.right = branch
    
    def setMid (self, branch):
        self.middle = branch

    

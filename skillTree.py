from branch import branch
class skillTree:

    activeEffects = []

    def _init_(self):
        self.root1 = branch(self, None, None, None, None)
        self.root2 = branch(self, None, None, None, None)
        self.root3 = branch(self, None, None, None, None)
    
    
    def getAllEffects (self, choice: int):
        if choice == 1:
            self.effectChecker(self.root1)
        elif choice == 2:
            self.effectChecker(self.root2)
        elif choice == 3:
            self.effectChecker(self.root3)
        else:
            return "error, invalid choice"

    def __effectChecker (self,branch: branch):
        if branch.getRight() == None & branch.getLeft() == None & branch.getMiddle() == None:
            if (branch.getEffect().isActive()): 
                self.activeEffects.append(branch.getEffect())
        if branch.getRight() != None:
            if (branch.getEffect().isActive()): 
                self.activeEffects.append(branch.getEffect())
                if (branch.getRight().getEffect().isActive()):
                    self.activeEffect.append(branch.getRight().getEffect())
                    self.effectChecker(branch.getRight())
        if branch.getLeft() != None:
            if branch.getEffect().isActive(): 
                self.activeEffects.append(branch.getEffect())
                if branch.getLeft().getEffect().isActive():
                    self.activeEffects.append(branch.getLeft().getEffect())
                    self.effectChecker(branch.getLeft())
        if branch.getMiddle() != None:
            if (branch.getEffect().isActive()): 
                self.activeEffects.append(branch.getEffect())
                if (branch.getMiddle().getEffect().isActive()):
                    self.activeEffects.append(branch.getMiddle().getEffect())
                    self.effectChecker(branch.getMiddle())

        return self.activeEffects

    
    

            
    

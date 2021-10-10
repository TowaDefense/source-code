from branch import branch
class skillTree:

    activeEffects = []

    def _init_(self):
        self.branch1 = branch(self, None, None, None, None)
        self.branch2 = branch(self, None, None, None, None)
        self.branch3 = branch(self, None, None, None, None)
    
    
    def getAllEffects (self,choice):
        if choice == 1:
            effectChecker(self.branch1)
        elif choice == 2:
            effectChecker(self.branch2)
        elif choice == 3:
            effectChecker(self.branch3)
        else:
            return "error, invalid choice"

    def effectChecker (self,branch):
        if branch.getRight() == None & branch.getLeft() == None & branch.getMiddle() == None: 
            self.activeEffects.append(branch.getEffect())
        if branch.getRight() != None:
            self.activeEffect.append(branch.getRight().getEffect())
            effectChecker(branch.getRight())
        if branch.getLeft() != None:
            self.activeEffect.append(branch.getLeft().getEffect())
            effectChecker(branch.getLeft())
        if branch.getMiddle() != None:
            self.activeEffect.append(branch.getMiddle().getEffect())
            effectChecker(branch.getMiddle())

            


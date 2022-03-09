from Landscape import LandscapeState
class TreeNode:
    def __init__(self, data, count):
        self.left = None
        self.mid = None
        self.right = None
        self.data = data
        self.count = count + 1


    """
    assignAll 
    
    Branches a default block type: used to determine the domains of the current root to keep or prune
    Used in heuristic, but later all branches are unassigned
    """
    def assignAll(self, matrix):        
        landscape1 = LandscapeState(matrix, len(self.data.state)-1)
        landscape2 = LandscapeState(matrix, len(self.data.state)-1)
        landscape3 = LandscapeState(matrix, len(self.data.state)-1)
        landscape1.addParentTile(self.data.state)
        landscape2.addParentTile(self.data.state)
        landscape3.addParentTile(self.data.state)
        landscape1.addBorderBlock()
        landscape2.addElBlock()
        landscape3.addFullBlock()
        self.left = TreeNode(landscape1, len(self.data.state)-1)
        self.mid = TreeNode(landscape2, len(self.data.state)-1)
        self.right = TreeNode(landscape3, len(self.data.state)-1)
    
    """
    assign

    Same concept as assignAll, but used to expand on a specified branch
    """
    def assign(self, matrix, branch):
        landscape = LandscapeState(matrix, len(self.data.state)-1)
        landscape.addParentTile(self.data.state)
        if branch == "left":
            landscape.addBorderBlock()
            self.left = TreeNode(landscape,len(self.data.state)-1)
        elif branch == "mid":
            landscape.addElBlock()
            self.mid = TreeNode(landscape,len(self.data.state)-1)
        elif branch == "right":
            landscape.addFullBlock()
            self.right = TreeNode(landscape,len(self.data.state)-1)


    """
    unassignAll

    Resets branches of current root node
    """
    def unassignAll(self):
        self.left = None
        self.mid = None
        self.right = None
        #self.count = self.count - 1
        




    
        
        
        



from Landscape import Landscape


class TreeNode:
    def __init__(self, data, count):
        self.left = None
        self.middle = None
        self.right = None
        self.data = data
        self.tmpCount = count+1
        self.count = count + 1
        if(self.tmpCount > 4):
            self.tmpCount = 0
    


class States:
    def __init__(self, matrix):
        self.root = TreeNode(Landscape(matrix,0),0)
        self.matrix = matrix

    
    def addStates(self,root):
        print(root.count)
        landscape1 = Landscape(self.matrix, root.tmpCount)
        landscape2 = Landscape(self.matrix, root.tmpCount)
        landscape3 = Landscape(self.matrix, root.tmpCount)
        landscape1.addBorderBlock()
        landscape2.addElBlock()
        landscape3.addFullBlock()
        root.left = TreeNode(landscape1,root.count)
        root.middle = TreeNode(landscape2, root.count)
        root.right = TreeNode(landscape3, root.count)
        
        
        
        


#class AC3:
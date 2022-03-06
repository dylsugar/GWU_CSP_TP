from Landscape import Landscape


class TreeNode:
    def __init__(self, data, count):
        self.left = None
        self.mid = None
        self.right = None
        self.data = data
        self.tmpCount = count+1
        self.count = count + 1
    


class States:
    def __init__(self, matrix):
        initScape = Landscape(matrix,0)
        initScape.addInitBlock()
        self.root = TreeNode(initScape,0)
        self.matrix = matrix

    
    def addStates(self,root):
        
        landscape1 = Landscape(self.matrix, root.tmpCount)
        landscape2 = Landscape(self.matrix, root.tmpCount)
        landscape3 = Landscape(self.matrix, root.tmpCount)
        landscape1.addParentTile(root.data.state)
        landscape2.addParentTile(root.data.state)
        landscape3.addParentTile(root.data.state)
        landscape1.addBorderBlock()
        landscape2.addElBlock()
        landscape3.addFullBlock()
        root.left = TreeNode(landscape1,root.count)
        root.mid = TreeNode(landscape2, root.count)
        root.right = TreeNode(landscape3, root.count)
        
        
        
        


#class AC3:
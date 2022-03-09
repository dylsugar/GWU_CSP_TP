"""
Landscape class represents data of TreeNode
"""
class LandscapeState:
    def __init__(self, matrix, tc):
        self.state = []
        self.tileCount = tc
        self.matrix = matrix
        self.miniMatrix = []


    def addInitBlock(self):
        ib = InitBlock(self.matrix)
        self.state.append(ib)

    def addBorderBlock(self):
        ob = OuterBoundaryBlock(self.matrix, self.tileCount)
        self.state.append(ob)
    
    def addElBlock(self):
        eb = ElBlock(self.matrix, self.tileCount)
        self.state.append(eb)

    def addFullBlock(self):
        fb = FullBlock()
        self.state.append(fb)

    """
    Calculate count of a color within a specific tile
    """
    def getColorCount(self,color):
        clist = []
        for innerState in self.state:
            for inner in innerState.blockVal:
                    clist.append(inner)

        return clist.count(color)
    

    """
    Calculate count of a specific block within the whole landscape
    """
    def getBlockCount(self,blockType):
        blockCount = 0
        for innerState in self.state:
            if type(innerState) == blockType:
                blockCount+=1
        return blockCount



    """
    Account for adding past parent values to current landscape 
    """
    def addParentTile(self,parent):
        self.state+=parent


    
    def printGoalState(self):
        print("\n\n##### Solution Found!!! #####\n\n")
        self.state.pop(0)
        for x in self.state:
            print(x.miniMatrix)



"""
Initial Block - Void value purpose of placeholding
"""
class InitBlock:
    def __init__(self, matrix):
        self.blockVal = [0,0]


"""
El Block Object
"""
class ElBlock:
    def __init__(self, matrix, count):
        self.blockVal = self.getElBlock(matrix,count)
    
    def getElBlock(self,matrix,count):
        
        miniMatrix = matrix[count]
        self.miniMatrix = miniMatrix
        currVals = [miniMatrix[1][1],miniMatrix[1][2],miniMatrix[1][3],miniMatrix[2][1],miniMatrix[2][2],miniMatrix[2][3],miniMatrix[3][1],miniMatrix[3][2],miniMatrix[3][3]]
        miniVal = []
        for x in currVals:
            if(x.isnumeric()):
                miniVal.append(int(x))
        return miniVal


"""
OuterBoundaryBlocks
"""
class OuterBoundaryBlock:
    def __init__(self,matrix,count):
        self.blockVal = self.getOuterBlock(matrix,count)

    def getOuterBlock(self,matrix,count):
        miniMatrix = matrix[count]
  
        self.miniMatrix = miniMatrix
        currVals = [miniMatrix[1][1], miniMatrix[1][2], miniMatrix[2][1], miniMatrix[2][2]]
        miniVal = []

        for x in currVals:
            if(x.isnumeric()):
                miniVal.append(int(x))

        return miniVal



"""
Full Block Block
"""
class FullBlock:
    def __init__(self):
        self.blockVal = []
        self.miniMatrix = []
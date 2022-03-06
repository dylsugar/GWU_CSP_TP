

from queue import Full


class Landscape:
    def __init__(self, matrix, tc):
        self.state = []
        self.tileCount = tc
        self.matrix = matrix
        self.bbCount = 0
        self.elCount = 0
        self.fbCount = 0
        #self.colorOne += self.getColorCount(1)
        #self.colorTwo += self.getColorCount(2)
        #self.colorThree += self.getColorCount(3)
        #self.colorFour += self.getColorCount(4)

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

    def getColorCount(self,color):
        clist = []
        for innerState in self.state:
            for inner in innerState.blockVal:
                    clist.append(inner)

        return clist.count(color)

    def addParentTile(self,parent):
        self.state+=parent

class InitBlock:
    def __init__(self, matrix):
        self.blockVal = [-1,-1]

class ElBlock:
    def __init__(self, matrix, count):
        self.blockVal = self.getElBlock(matrix,count)
    
    def getElBlock(self,matrix,count):
        miniMatrix = matrix[count-1]

        #print("Count:",count-1)
        #print("MM: ",miniMatrix)
        currVals = [miniMatrix[1][1],miniMatrix[1][2],miniMatrix[1][3],miniMatrix[2][1],miniMatrix[2][2],miniMatrix[2][3],miniMatrix[3][1],miniMatrix[3][2],miniMatrix[3][3]]
        #print("currVals: ",currVals)
        #print("el block: ",currVals)
        miniVal = []
        for x in currVals:
            if(x.isnumeric()):
                miniVal.append(int(x))
        return miniVal


class OuterBoundaryBlock:
    def __init__(self,matrix,count):
        self.blockVal = self.getOuterBlock(matrix,count)

    def getOuterBlock(self,matrix,count):
        miniMatrix = matrix[count-1]
        currVals = [miniMatrix[1][1],miniMatrix[1][2],miniMatrix[2][1],miniMatrix[2][2]]
        #print("outer block:",currVals)
        miniVal = []
        for x in currVals:
            if(x.isnumeric()):
                miniVal.append(int(x))
        return miniVal

class FullBlock:
    def __init__(self):
        self.blockVal = []
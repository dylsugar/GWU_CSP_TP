

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


    def addBorderBlock(self):
        ob = OuterBoundaryBlock(self.matrix, self.tileCount)
        self.state.append(ob)
        self.bbCount+=1
        #self.tileCount+=1
    
    def addElBlock(self):
        eb = ElBlock(self.matrix, self.tileCount)
        self.state.append(eb)
        self.elCount+=1
        #self.tileCount+=1

    def addFullBlock(self):
        fb = FullBlock()
        self.state.append(fb)
        self.fbCount+=1
        #self.tileCount+=1
    
    def getColorCount(self,color):
        clist = []
        for innerState in self.state:
            for inner in innerState.blockVal:
                clist.append(inner)
        
        return clist.count(color)

class ElBlock:
    def __init__(self, matrix, count):
        self.blockVal = self.getElBlock(matrix,count)
    
    def getElBlock(self,matrix,count):
        miniMatrix = matrix[count]
        currVals = [miniMatrix[1][1],miniMatrix[1][2],miniMatrix[1][3],miniMatrix[2][1],miniMatrix[2][2],miniMatrix[2][3],miniMatrix[3][1],miniMatrix[3][2],miniMatrix[3][3]]
        miniVal = []
        for x in currVals:
            if(x.isnumeric()):
                miniVal.append(int(x))
        return miniVal


class OuterBoundaryBlock:
    def __init__(self,matrix,count):
        self.blockVal = self.getOuterBlock(matrix,count)

    def getOuterBlock(self,matrix,count):
        # return sum of color available after outer boundary tile is used
        #for x in matrix:
        #    print(x)
        #print(matrix[4])
        #print("Count: ",count)
        #print(matrix)
        miniMatrix = matrix[count-1]
        currVals = [miniMatrix[1][1],miniMatrix[1][2],miniMatrix[2][1],miniMatrix[2][2]]
        miniVal = []
        for x in currVals:
            if(x.isnumeric()):
                miniVal.append(int(x))
        return miniVal

class FullBlock:
    def __init__(self):
        self.blockVal = []
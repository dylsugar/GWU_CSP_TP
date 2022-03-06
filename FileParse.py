import copy
from selectors import EpollSelector
import numpy as np



class Parser:
    def parse(self, path):
        fp = open(path,"r")
        line = fp.readline()
        line = fp.readline()
        count = 1
        fList = []
        size = 0

        landscape = False
        Tile = False
        Target = False

        while line:
            #if("# Landscape" in line):
            #    continue
                
            #elif("# Tiles:" in line):
            #    print("tiles true")
            #    landscape = False
            #    Tile = True
            #elif("# Targets" in line):
            #    print("Targets true")
            #    Target = True
            #    Tile = False
            
            #if landscape:
            outstring = ""
            line = line.strip("\n")
            for i in range(0,len(line)):
                if(i%2==0):
                    outstring+=line[i]+"."

            fArray = outstring.split(".")
            fArray.pop()
            size = len(fArray)/4
            result=[fArray[i:i + 4] for i in range(0, len(fArray), 4)]
            if result:
                fList.append(result)
            line = fp.readline()
            count+=1
            #elif Tile:
                #line = fp.readline()
            #elif Target:
                #line = fp.readline()
        ct = 0

        #for x in fList:
        #    print(x)
        #    ct+=1
        #print(ct)
        fullMatrix = []
        #print(size)
        for x in range(0,int(size*5)):
            fullMatrix.append([])

        bc = 0
        cnt = 0
        shallowCount = 0
        
        for x in range(0,5):
            for y in range(0,int(size*4)):
                if(len(fullMatrix[cnt]) > 3):
                    cnt+=1
                #print("flist: ",y," ",len(fList))
                fullMatrix[cnt].append(fList[y][x])
                #print("CNT: ",fullMatrix[cnt])#,"||||||",fList[y])
                #print(cnt," ",y)
        
                


        
        #for x in fullMatrix:
        #    print(x)

        return fullMatrix, size*size





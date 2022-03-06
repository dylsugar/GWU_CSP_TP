import copy
from selectors import EpollSelector
import numpy as np



class Parser:
    def parse(self, path):
        fp = open(path,"r")
        line = fp.readline()
        line = fp.readline()
        line = fp.readline()
        count = 1
        fList = []
        size = 0

        while line:
            if("# Tiles:" in line):
                break
            
            outstring = ""
            line = line.strip("\n")
            for i in range(0,len(line)):
                if(i%2==0):
                    outstring+=line[i]+"."

            fArray = outstring.split(".")
            fArray.pop()
            if(fArray):
                size = len(fArray)/4
            result=[fArray[i:i + 4] for i in range(0, len(fArray), 4)]
            if result:
                fList.append(result)
            line = fp.readline()
            count+=1

        newline = fp.readline()
        tileList = []
        while newline:
            if("# Targets" in newline):
                break
            tmp = newline.replace("OUTER_BOUNDARY=","")
            tmp = tmp.replace("EL_SHAPE=","")
            tmp = tmp.replace("FULL_BLOCK=","")
            tmp = tmp.replace("}","")
            tmp = tmp.replace("{","")
            tmp = tmp.strip("\n")
            tmp = tmp.split(", ")
            tileList = [int(i) for i in tmp]
            newline = fp.readline()
            newline = fp.readline()

        lastLine = fp.readline()
        targetList = []
        while lastLine:
            singleTarget = lastLine.split(":")
            targetList.append((int(singleTarget[0].strip()),int(singleTarget[1].strip())))
            lastLine = fp.readline()



        fullMatrix = []
        for x in range(0,int(size*5)):
            fullMatrix.append([])
        
        cnt = 0
        for x in range(0,5):
            for y in range(0,int(size*4)):
                if(len(fullMatrix[cnt]) > 3):
                    cnt+=1
                fullMatrix[cnt].append(fList[y][x])

        return fullMatrix, size*size, tileList, targetList





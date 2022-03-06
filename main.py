from FileParse import Parser
from States import States



def populateStates(states,root, numTiles, targetCount):
    if(root.count > numTiles):
        return
    states.addStates(root)
    #print((states.root.left.data.state)[0].outerBlock)
    #print((states.root.middle.data.state)[0].elBlock)
    #print(root.data.state)
    if(root.data.getColorCount(1) > targetCount[0][1]):
        return
    if(root.data.getColorCount(2) > targetCount[1][1]):
        return
    if(root.data.getColorCount(3) > targetCount[2][1]):
        return
    if(root.data.getColorCount(4) > targetCount[3][1]):
        return
    
    print("rootdata:",root.data.getColorCount(1)," ",root.data.getColorCount(2)," ",root.data.getColorCount(3)," ",root.data.getColorCount(4))
    #print(root.data.state)
    if(root.data.getColorCount(1) == targetCount[0][1]):
        if(root.data.getColorCount(2) == targetCount[1][1]):
            if(root.data.getColorCount(3) == targetCount[2][1]):
                if(root.data.getColorCount(4) == targetCount[3][1]):
                    print("Solution Found")
                    exit()

    populateStates(states, root.left, numTiles,targetCount)

    populateStates(states, root.mid, numTiles,targetCount)

    populateStates(states, root.right, numTiles,targetCount)

    

if __name__ == "__main__":
    path = "test0.txt"
    p = Parser()
    matrix, numTiles, tilesCount, targetCount = p.parse(path)
    # List of all possible states implemented with a Tree
    print("MATRIX: ")
    for x in matrix: 
        print(x)
    print("NUM_TILES: ",numTiles)
    print("EACH_TILE: ", tilesCount)
    print("TARGET_TILE: ",targetCount)
    states = States(matrix)
    
    #states.addStates(states.root)
    
    #print(states.root.data.state)
    #rr = states.root.mid
    #print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left
    #print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right
    #print("Full Block",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid
    #print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid.mid
    #print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    
    #rr = states.root.mid.left.right.mid.mid.right
    #print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid.mid.right.mid
    #print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid.mid.right.mid.left
    #print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid.mid.right.mid.left.left
    #print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid.mid.right.mid.left.left.right
    #print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))

    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid.mid.right.mid.left.left.right.left
    #print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #states.addStates(rr)
    #rr = states.root.mid.left.right.mid.mid.right.mid.left.left.right.left.right
    #print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    #print(targetCount[0][1])
    #print(targetCount[1][1])
    #print(targetCount[2][1])
    #print(targetCount[3][1])
    populateStates(states, states.root, numTiles, targetCount)




    




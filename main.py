from FileParse import Parser
from States import States

# Slack questions: 


def populateStates(states,root, numTiles):
    if(root.count > numTiles):
        return
    states.addStates(root)
    #print((states.root.left.data.state)[0].outerBlock)
    #print((states.root.middle.data.state)[0].elBlock)
    #print(root.data.state)
    if(root.data.getColorCount(1) > 18):
        return
    if(root.data.getColorCount(2) > 19):
        return
    if(root.data.getColorCount(3) > 16):
        return
    if(root.data.getColorCount(4) > 17):
        return
    
    print("rootdata:",root.data.getColorCount(1)," ",root.data.getColorCount(2)," ",root.data.getColorCount(3)," ",root.data.getColorCount(4))
    #print(root.data.state)
    if(root.data.getColorCount(1) == 18):
        if(root.data.getColorCount(2) == 19):
            if(root.data.getColorCount(3) == 16):
                if(root.data.getColorCount(4) == 17):
                    print("Solution Found")
                    exit()

    populateStates(states, root.left, numTiles)

    populateStates(states, root.mid, numTiles)

    populateStates(states, root.right, numTiles)
    #else:
    #    return
    

if __name__ == "__main__":
    path = "test0.txt"
    p = Parser()
    matrix, numTiles = p.parse(path)
    # List of all possible states implemented with a Tree
    #for x in matrix: 
    #    print(x)
    
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
    
    populateStates(states, states.root, numTiles)




    




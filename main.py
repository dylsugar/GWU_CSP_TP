from FileParse import Parser
from States import States

# Slack questions: 


def populateStates(states,root, numTiles):
    
    states.addStates(root)
    #print((states.root.left.data.state)[0].outerBlock)
    #print((states.root.middle.data.state)[0].elBlock)
    #print("rootdata:",root.data.getColorCount(1)," ",root.data.getColorCount(2)," ",root.data.getColorCount(3)," ",root.data.getColorCount(4))
    print(root.data.state)
    if(root.data.getColorCount(1) == 18):
        if(root.data.getColorCount(2) == 19):
            if(root.data.getColorCount(3) == 16):
                if(root.data.getColorCount(4) == 17):
                    print("Solution Found")
                    exit()

    if(root.count < numTiles):
        populateStates(states, root.left, numTiles)
    else:
        return
    
            
    if(root.count < numTiles):
        populateStates(states, root.middle, numTiles)
    else:
        return


    if(root.count < numTiles):
        populateStates(states, root.right, numTiles)
    else:
        return
    

if __name__ == "__main__":
    path = "test0.txt"
    p = Parser()
    matrix, numTiles = p.parse(path)
    # List of all possible states implemented with a Tree
    print(matrix)
    states = States(matrix)
    print(states.root)
    states.addStates(states.root)
    print("Left: ",states.root.left.data.state[0].blockVal)
    print("Middle: ",states.root.middle.data.state[0].blockVal)
    print("Right:",states.root.right.data.state[0].blockVal)
    states.addStates(states.root.left)
    print(states.root.left.data.state[0].blockVal)
    print(states.root.left.left.data.state[0].blockVal)
    print(states.root.left.middle.data.state[0].blockVal)
    print(states.root.left.right.data.state[0].blockVal)
    #print(states.root.left.left.data.state[0].blockVal)
    #print(states.root.left.middle.data.state[0].blockVal)
    #print(states.root.left.middle.data.state[1].blockVal)
    #print(states.root.left.right.data.state[0].blockVal)
    #print(states.root.left.right.data.state[1].blockVal)
    #populateStates(states, states.root, numTiles)




    




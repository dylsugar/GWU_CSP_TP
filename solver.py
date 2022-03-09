from asyncio.proactor_events import _ProactorDuplexPipeTransport
from time import time

from paramiko import PasswordRequiredException
from FileParse import Parser
from TreeState import TreeNode
from Landscape import LandscapeState, ElBlock, OuterBoundaryBlock, FullBlock
from backtrack import backtrack_recursive, targetCheck
import time


def solve(matrix):
    print("####### Project 2 : Constraint Satisfaction Propagation Tile Placement #######\n")
    print("Searching for solution...")
    # Initialize Tree of landscapes in different states: class will represent head node of tree that holds consecutive states
    initScape = LandscapeState(matrix, 0)
    initScape.addInitBlock()
    root = TreeNode(initScape,0)
    # AC3 Algorithm

    # AC3 Algorithm conditional if exists

    # Backtrack Search Algorithm w/ LCV Heuristic
    backtrack_recursive(matrix, root, numTiles, tilesCount, targetCount)
    
    




if __name__ == "__main__":
    path = "test0.txt"
    p = Parser()
    matrix, numTiles, tilesCount, targetCount = p.parse(path)
    # List of all possible states implemented with a Tree
    print("MATRIX: ")
    for x in matrix: 
        print(x)
    print("NUM_TILES: ",numTiles)
    print("OUTER BOUNDARY Count: ",tilesCount[0],", EL SHAPE COUNT: ",tilesCount[1],", FULL BLOCK Count: ",tilesCount[2])
    print("TARGET_TILE (Bush): ",targetCount)
    
    solve(matrix)


    """
    root.assignAll(matrix)
    rr = root.mid
    print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left
    print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right
    print("Full Block",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid
    print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid
    print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    
    rr = root.mid.left.right.mid.mid.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid
    print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left
    print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left
    print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left
    print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left
    print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid
    print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right.left
    print("Border Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right.left.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right.left.right.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right.left.right.right.mid
    print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right.left.right.right.mid.right
    print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    rr.assignAll(matrix)
    rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right.left.right.right.mid.right.mid
    print("El Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    populateStates(matrix, rr, numTiles, targetCount)
    #rr.assignAll(matrix)
    #rr = root.mid.left.right.mid.mid.right.mid.left.left.right.left.right.right.left.right.mid.right.right.left.right.right.mid.right.mid.right
    #print("Full Block Data:",rr.data.getColorCount(1)," ",rr.data.getColorCount(2)," ",rr.data.getColorCount(3)," ",rr.data.getColorCount(4))
    """

    



    




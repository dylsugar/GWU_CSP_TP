from heuristic import order_domain_values
from Landscape import ElBlock, OuterBoundaryBlock, FullBlock

"""
Backtracking Search Algorithm

if assignment is complete then return true
var = select unassigned variable(csp)
for values in order_domain_values(var, assignment, csp):
    if adding var = val satisfies every constraint then
        assign values
        result = recurse(assign, state)
        if result then return
        unassign values

"""
def backtrack_recursive(matrix, root, numTiles, tilesCount, targetCount):
    if not root:
        return
    if(root.count >= numTiles):
       return
    
    if(targetCheck(root, numTiles, tilesCount, targetCount)):
        root.data.printGoalState()
        print("Color Target Final State:",root.data.getColorCount(1)," ",root.data.getColorCount(2)," ",root.data.getColorCount(3)," ",root.data.getColorCount(4))
        print("Tile Target Final State:",root.data.getBlockCount(ElBlock)," ",root.data.getBlockCount(OuterBoundaryBlock)," ",root.data.getBlockCount(FullBlock),"\n")
        exit()

    
    for branch in order_domain_values(matrix, root, numTiles, tilesCount, targetCount):
        # assign 3 block types to the next available tile
        root.assign(matrix, branch)
        if branch == "left":
            branch = root.left
        elif branch == "mid":
            branch = root.mid
        elif branch == "right":
            branch = root.right


        # result should be based on details given in particular landscape
        backtrack_recursive(matrix, branch, numTiles, tilesCount, targetCount)



    
"""
targetCheck

Checks if current node has reached the goal state 
"""
def targetCheck(root, numTiles, tilesCount, targetCount):
    
    if(root.data.getColorCount(1) == targetCount[0][1]):
        if(root.data.getColorCount(2) == targetCount[1][1]):
            if(root.data.getColorCount(3) == targetCount[2][1]):
                if(root.data.getColorCount(4) == targetCount[3][1]):
                    if root.count == numTiles-1:
                        root.data.addFullBlock() 
                    if(root.data.getBlockCount(OuterBoundaryBlock) == tilesCount[0]):
                        if(root.data.getBlockCount(ElBlock) == tilesCount[1]):
                            if(root.data.getBlockCount(FullBlock) == tilesCount[2]):
                                return True
    return False
from Landscape import ElBlock, OuterBoundaryBlock, FullBlock

"""
Least Constraining Value (LCV) heuristic

Definition: variable that rules out the fewest values in remaining variables

Idea: When arriving at a root node, go to the branch that 
has the possibility to use all types of blocks at most and
isn't constrained to use just 1 type of block. In backtracking,
we need to check children LCV to determine this.

"""

def order_domain_values(matrix, root, numTiles, tilesCount, targetCount):
    if root.count >= numTiles-1:
        return []
    root.assignAll(matrix)
    lc = getConstraintChoices(matrix, root.left, numTiles, tilesCount, targetCount)
    mc = getConstraintChoices(matrix, root.mid, numTiles, tilesCount, targetCount)
    rc = getConstraintChoices(matrix, root.right, numTiles, tilesCount, targetCount)
    
    branchList = ['left','mid','right']
    choiceList = [len(lc),len(mc),len(rc)]
    minChoice = min(choiceList)

    if(choiceList.count(minChoice) != len(choiceList)):
        for x in range(choiceList.count(minChoice)):
            branchList.pop(choiceList.index(minChoice))
    root.unassignAll()
    return branchList


"""
Per root node, a list of available tiles will be available
to choose based on the constraints that the child node 
1. does not have a sum tile count greater than the allowed
2. color count after specified block placement within tile
    does not exceed the given color target number
"""
def getConstraintChoices(matrix, root, numTiles, tilesCount, targetCount):

    root.assignAll(matrix)
    children = [root.left, root.mid, root.right]
    finalChildren = []
    for child in children:

        if(child.data.getColorCount(1) > targetCount[0][1]):
            continue
        if(child.data.getColorCount(2) > targetCount[1][1]):
            continue
        if(child.data.getColorCount(3) > targetCount[2][1]):
            continue
        if(child.data.getColorCount(4) > targetCount[3][1]):
            continue
        
        if(child.data.getBlockCount(OuterBoundaryBlock) > tilesCount[0]):
            continue
        if(child.data.getBlockCount(ElBlock) > tilesCount[1]):
            continue
        if(child.data.getBlockCount(FullBlock) > tilesCount[2]):
            continue
        
        if child == root.left:
            finalChildren.append('left')
        elif child == root.mid:
            finalChildren.append('mid')
        elif child == root.right:
            finalChildren.append("right")
    return finalChildren

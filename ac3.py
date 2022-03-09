from heuristic import getConstraintChoices
# Constraint Propagation AC3

def AC3(matrix, root, numTiles, tilesCount, targetCount, queue=None):
    
    if queue == None:
        queue = list(getConstraintChoices(matrix, root, numTiles, tilesCount, targetCount))

    while queue:

        child = queue.pop(0)
        if child == "left":
            child = root.left
        elif child == "right":
            child = root.right
        elif child == "mid":
            child = root.mid
        
        child.assignAll(matrix)

        if len(getConstraintChoices(matrix, child, numTiles, tilesCount, targetCount)) == 1:
                return False
        for neighbor in getConstraintChoices(matrix, root, numTiles, tilesCount, targetCount):
            queue.append(neighbor)
        return False

                
        
# Constraint Satisfaction Problem: Tile Placement
Dylan Suga

# Problem: 
We are given a 2D array of NxN size each with tiles with cells 4x4. A cell can contain the values 1-4 which represent colors. In each tile, we can use an El shaped block, outer boundary block, or a full block where each shows or doesn’t show a section of the tile known as a bush. Given target values for colors (count of a certain exposed color within a bush) and count for types of specified tiles, this program has to find a way to fill the desired landscape with a combination of different tiles to match the target values.

# Command-line execute : python3 solver.py

Txt file can be changed in solver.py in __main__ method under path variable. It is set to "test0.txt" at the moment.

# JUnit test execute : python3 tests.py

# Structure:
There are two main objects within the program, TreeNode and Landscape. As implied by its name, the TreeNode represents a root node of a tree with 3 branches for the 3 different types of Tile blocks (El, Outer Boundary, Full). Each TreeNode thus holds a Landscape object. The Landscape object represents a state where one can add different types of block to different states. The different states are held in the ‘state’ attribute of Landscape. The Landscape module also holds objects of the three different tile types. A landscape thus holds different combinations of these tiles and the count of the targeted color values. 

# Algorithm Explanation:
Using a tree implementation, I used the Backtracking Search Algorithm to find the solution. Each node in the tree represented a different landscape where the children of the parent node would have one of the three specified tiles placed in landscape in a consecutive block. To supplement this, I used the Least Constraining Value heuristic such that it would check the children of the root node and based on the generated constraints, each child would return back a length of the number of possible branches available without breaking the constraint. Since I want to pick the branches with the least constraining value, I would pick the branch/child that returns the largest number of possibilities. The constraints are based off of the target value and the maximum number of tiles allowed considering the dimensions of the matrix. If a particular node has a count of tiles greater than the maximum count, then that branch is pruned. If a particular node exceeds the threshold of one of the target values for a color or tile type, then that branch will be pruned since there is no way for that value to decrease. The values can be reached through the getColorCount() and getBlockCount() in the Landscape class. For each tile object such as a ElBlock or OuterBoundaryBlock, a ‘blockVal’ attribute is a list that only accounts for the colors 1-4 and removes blank spaces for a single tile. 


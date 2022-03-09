import unittest
from Landscape import FullBlock, LandscapeState, ElBlock, OuterBoundaryBlock
from TreeState import TreeNode

"""
JUnit Tests for Landscape class and TreeNode class
"""
class UnitTests(unittest.TestCase):

    # Test if different blocks are added correctly to a Landscape object
    def test_block_creation(self):
        test_matrix = [[['1','2','1','2'],['2','3','2','3'],['3','4','3','4'],['4','4','4','4']]]
        test_landscape1 = LandscapeState(test_matrix,0)
        test_landscape1.addElBlock()
        self.assertEqual(type(test_landscape1.state[0]),ElBlock)

        test_landscape2 = LandscapeState(test_matrix,0)
        test_landscape2.addBorderBlock()
        self.assertEqual(type(test_landscape2.state[0]),OuterBoundaryBlock)
        
        test_landscape3 = LandscapeState(test_matrix,0)
        test_landscape3.addFullBlock()
        self.assertEqual(type(test_landscape3.state[0]),FullBlock)
    
    # Test if specified color count of a tile works after different block placements
    def test_color_count(self):
        test_matrix = [[['1','2','1','2'],['2','3','2','3'],['3','4','3','4'],['4','4','4','4']]]
        test_landscape1 = LandscapeState(test_matrix,0)
        test_landscape1.addElBlock()
        self.assertEqual(test_landscape1.getColorCount(1),0)
        self.assertEqual(test_landscape1.getColorCount(2),1)
        self.assertEqual(test_landscape1.getColorCount(3),3)
        self.assertEqual(test_landscape1.getColorCount(4),5)


        test_landscape2 = LandscapeState(test_matrix,0)
        test_landscape2.addBorderBlock()
        self.assertEqual(test_landscape2.getColorCount(1),0)
        self.assertEqual(test_landscape2.getColorCount(2),1)
        self.assertEqual(test_landscape2.getColorCount(3),2)
        self.assertEqual(test_landscape2.getColorCount(4),1)
        
        test_landscape3 = LandscapeState(test_matrix,0)
        test_landscape3.addFullBlock()
        self.assertEqual(test_landscape3.getColorCount(1),0)
        self.assertEqual(test_landscape3.getColorCount(2),0)
        self.assertEqual(test_landscape3.getColorCount(3),0)
        self.assertEqual(test_landscape3.getColorCount(4),0)
    
    
    # Test if blocks are properly accumulated within a Landscape.state attribute
    def test_block_count(self):
        test_matrix = [[['1','2','1','2'],['2','3','2','3'],['3','4','3','4'],['4','4','4','4']]]
        test_landscape = LandscapeState(test_matrix,0)
        test_landscape.addBorderBlock()
        test_landscape.addElBlock()
        test_landscape.addFullBlock()
        test_landscape.addBorderBlock()
        test_landscape.addElBlock()
        test_landscape.addFullBlock()
        test_landscape.addBorderBlock()
        test_landscape.addBorderBlock()
        test_landscape.addElBlock()
        test_landscape.addElBlock()
        test_landscape.addBorderBlock()
        self.assertEqual(test_landscape.getBlockCount(ElBlock),4)
        self.assertEqual(test_landscape.getBlockCount(OuterBoundaryBlock),5)
        self.assertEqual(test_landscape.getBlockCount(FullBlock),2)

    # Test if children nodes are properly assigned a block
    def test_assign_all(self):
        test_matrix = [[['1','2','1','2'],['2','3','2','3'],['3','4','3','4'],['4','4','4','4']]]
        initScape = LandscapeState(test_matrix, 0)
        initScape.addInitBlock()
        root = TreeNode(initScape,0)
        root.assignAll(test_matrix)
        self.assertEqual(type(root.left.data.state[1]),OuterBoundaryBlock)
        self.assertEqual(type(root.mid.data.state[1]),ElBlock)
        self.assertEqual(type(root.right.data.state[1]),FullBlock)

    # Test if children node values can be voided
    def test_unassign_all(self):
        test_matrix = [[['1','2','1','2'],['2','3','2','3'],['3','4','3','4'],['4','4','4','4']]]
        initScape = LandscapeState(test_matrix, 0)
        initScape.addInitBlock()
        root = TreeNode(initScape,0)
        root.assignAll(test_matrix)
        root.unassignAll()
        self.assertEqual(root.left,None)
        self.assertEqual(root.mid,None)
        self.assertEqual(root.right,None)




if __name__=="__main__":
    unittest.main()
    #test_get_block_count()
    #test_block_creation()
    #test_assign_all()
    #test_unassign_all()

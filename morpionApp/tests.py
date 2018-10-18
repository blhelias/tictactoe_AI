from django.test import TestCase
from . IAMorpion import minimax
# import unittest
# Create your tests here.
###########################################################################
#TEST
###########################################################################
# test empty index  
class IATestCase(TestCase):
    # test empty condition
    def test_find_empty(self):   
        test_board1 = [0, 0, 1, 2, 0 ,2, 1, 0, 0]
        test_board2 = [0, 1, 1, 2, 1 ,2, 1, 2, 0]
        self.assertEqual(minimax.empty_indexes(test_board1), [0, 1, 4, 7, 8])
        self.assertEqual(minimax.empty_indexes(test_board2), [0, 8])

    # test win conditions
    def test_win_conditions(self):
        test_board3 = [1, 1, 1, 2, 0 ,2, 1, 0, 0]
        test_board4 = [2, 0, 1, 2, 2 , 0, 1, 0, 2]
        self.assertTrue(minimax.check_win(test_board3, 1))
        self.assertFalse(minimax.check_win(test_board3, 2)) # False
        self.assertFalse(minimax.check_win(test_board4, 1)) # False
        self.assertTrue(minimax.check_win(test_board4, 2)) # True

    def test_minimax(self):
        # test minimax
        # 1
        init_board = [1, 0, 0, 0, 0 ,0, 0, 0, 0]
        print(minimax(init_board, ai_player))
        # 2
        board_stage_1 = [1, 0, 0, 0, 2 ,0, 1, 0, 0]
        print(minimax(board_stage_1, ai_player))
        # 3
        board_stage_2 = [1, 0, 0, 2, 2, 1, 1, 0, 0]
        print(minimax(board_stage_2, ai_player))
        # 4
        board_stage_3 = [1, 2, 0, 2, 2, 1, 1, 1, 0]
        print(minimax(board_stage_3, ai_player))
        # 5
        board_stage_3 = [1, 2, 0, 2, 2, 1, 1, 1, 2]
        print(minimax(board_stage_3, ai_player))
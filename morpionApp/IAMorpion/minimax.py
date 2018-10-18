# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:53:53 2018

@author: brieuc.lhelias
"""
from typing import List, Dict

hu_player = 1
ai_player = 2

def empty_indexes(board: List[int]) -> List[int]:
    """
    return a list of empty indexes in an array
    """
    res = []
    for count, element in enumerate(board):
        if element == 0:
            res.append(count) 
    return res

def check_win(board: List[int], player: int) -> bool:
    l1 = [board[0], board[1], board[2]]
    l2 = [board[3], board[4], board[5]]
    l3 = [board[6], board[7], board[8]]
    c1 = [board[0], board[3], board[6]]
    c2 = [board[1], board[4], board[7]]
    c3 = [board[2], board[5], board[8]]
    d1 = [board[0], board[4], board[8]]
    d2 = [board[2], board[4], board[6]]
    end = [l1, l2, l3, c1, c2, c3, d1, d2]

    for i in end:
        if i[0] == i[1] == i[2] == player:
            return True
        
    return False

def minimax(new_board: List[int], player: int) -> Dict:
    avail_spots = empty_indexes(new_board)
    # check for the terminal states such as win, lose, and tie
    # and return a value accordingly
    if check_win(new_board, hu_player):
        return {"score": -10}

    elif check_win(new_board, ai_player):
        return {"score": 10}
    
    elif len(avail_spots) == 0:
        return {"score": 0}
    
    # an array to collect all the objects    
    moves = []
    for i in range(len(avail_spots)):
        # create an object for each and store the index of that spot        
        move = {}
        move["index"] = avail_spots[i]
        
        # set the empty spot to the current player    
        new_board[avail_spots[i]] = player
        
        # colect the score resulted from calling minimax
        # on the opponent of the current player    
        if player == ai_player:
            result = minimax(new_board, hu_player)
            move["score"] = result["score"]
        else:
            result = minimax(new_board, ai_player)
            move["score"] = result["score"]
        
        # reset the spot to empty
        new_board[avail_spots[i]] = 0
        # push the object to the array

        moves.append(move)

    # if it is the computer's turn, loop over the moves and
    # choose the move with the highest score
    if player == ai_player:
        best_score = -10000

        for i in range(len(moves)):
            if moves[i]["score"] > best_score:
                best_score = moves[i]["score"]
                best_move = i        
    else:
        best_score = 10000
        for i in range(len(moves)):
            if moves[i]["score"] < best_score:
                best_score = moves[i]["score"]
                best_move = i

    return moves[best_move]

def reformat_response_board(board: List[int], choice) -> List[int]:
    x, y = choice // 3, choice % 3
    board[x][y]['value'] = 2
    return board

def convert_requested_board(board: List[int]) -> List[int]:
    res = []
    for i in range(3):
        for j in range(3):
            res.append(board[i][j]['value'])
    return(res)

def main(requested_board: List[int]) -> List[int]:
    board = convert_requested_board(requested_board)
    result = minimax(board, ai_player)
    board[result["index"]] = 2
    choice = result["index"]
    data = reformat_response_board(requested_board, choice)
    return data, result["index"], result["score"]

if __name__ == "__main__":
    ###########################################################################
    #TEST
    ###########################################################################
    # test empty index       
    test_board1 = [0, 0, 1, 2, 0 ,2, 1, 0, 0]
    test_board2 = [0, 1, 1, 2, 1 ,2, 1, 2, 0]
    print(empty_indexes(test_board1)) # [0, 1, 4, 7, 8]
    print(empty_indexes(test_board2)) # [0, 8]
    
    # test win conditions
    test_board3 = [1, 1, 1, 2, 0 ,2, 1, 0, 0]
    test_board4 = [2, 0, 1, 2, 2 , 0, 1, 0, 2]
    print(check_win(test_board3, 1)) # True
    print(check_win(test_board3, 2)) # False
    print(check_win(test_board4, 1)) # False 
    print(check_win(test_board4, 2)) # True
    
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
    
    
    

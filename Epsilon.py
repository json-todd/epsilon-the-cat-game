from random import randint
import Board

class Epsilon:
    def __init__(self, Board):
        self.x_Eps, self.y_Eps = [randint(0, Board.size - 1) for i in range(2)]
        self.parent_board = Board

    def update_pos_on_board(self):
        self.parent_board[self.y_Eps][self.x_Eps] = str(self)
        
    def move_up(self):
        if self.y_Eps == 0: return
        
        self.y_Eps -= 1
    def move_down(self):
        if self.x_Eps == 0: return
        self.x_Eps -= 1
    def move_left(self):
        if self.y_Eps == Board.size - 1: return
        self.y_Eps += 1
    def move_right(self):
        if self.x_Eps == Board.size - 1: return
        self.x_Eps += 1    

    def __str__(self):
        return '🐈'
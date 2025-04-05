from Board import BoardPiece, SquareBoard
from random import randint

class Food(BoardPiece):
    def __init__(self, board):
        self.x = randint(0, board.size - 1)
        self.y = randint(0, board.size - 1)

        super().__init__(
            str(self),
            self.x,
            self.y,
            board
        )
        
    def __str__(self):
        return '🥩'


if __name__ == '__main__':
    board_test = SquareBoard(5)
    food_test = Food(board_test)

    # Food has an attribute with name 'board'
    assert hasattr(food_test, 'board')
    # the 'board' is an instance of SquareBoard class
    assert isinstance(getattr(food_test, 'board'), SquareBoard), '`board` is not an instance of `SquareBoard` class'

    # the positions of Food are integer
    assert all(isinstance(_elem, int) for _elem in food_test.get_pos()), 'location does not follow format of (int, int)'
    # all positions Food are in the range of board size
    assert all(_elem < food_test.board.size for _elem in food_test.get_pos()), 'Food is out of board'

    


    
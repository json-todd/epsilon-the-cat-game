from random import randint
from Board import SquareBoard, BoardPiece


class Epsilon(BoardPiece):

    def __init__(self, board):
        """A cute cat. She's the main star of our game
        When game starts, her entrance to the board is random

        param:
            board: Board, the game board where Epsilon is placed on
        """
        x_Eps, y_Eps = [
            randint(
                0, board.size - 1) \
            for i in range(2)
        ]
        super().__init__(str(self), x_Eps, y_Eps, board)

    def move_up(self):
        if self.y_pos == 0: return
        self.y_pos -= 1

    def move_down(self):
        if self.x_Eps == 0: return
        self.x_Eps -= 1

    def move_left(self):
        if self.y_pos == self.board.size - 1: return
        self.y_pos += 1

    def move_right(self):
        if self.x_Eps == self.board.size - 1: return
        self.x_Eps += 1

    def __str__(self):
        return '🐈'


if __name__ == '__main__':
    board_test = SquareBoard(5)

    # [case]: instantiate Epsilon
    for _test in range(10):
        try:
            # print(f'Case #{_test}:')
            eps_test = Epsilon(board_test)
            
            # Epsilon has an attribute with name 'board'
            assert hasattr(eps_test, 'board'), 'Epsilon is not on any board'
            # the 'board' is an instance of BoardPiece class
            assert isinstance(getattr(eps_test, 'board'), SquareBoard), 'board is not a SquareBoard'
            assert all(isinstance(_elem, int) for _elem in eps_test.get_pos())
            assert all(_elem < board_test.size for _elem in eps_test.get_pos())
    
            # print(str(eps_test))
            # print(eps_test.get_pos())
            # print()
        except AssertionError as assert_error:
            print(f'Failure at #{_test}.\nThis occurs: {str(assert_error)}')
            print(eps_test.get_pos())

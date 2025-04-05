from random import randint
from Board import SquareBoard, BoardPiece
from test_util import run_a_test_many_times


class Epsilon(BoardPiece):

    def __init__(self, board):
        """A cute cat. She's the main star of our game
        When game starts, her entrance to the board is random

        param:
            board: Board, the game board where Epsilon is placed on
        """
        x_Eps = randint(0, board.size - 1)
        y_Eps = randint(0, board.size - 1)
        super().__init__(str(self), x_Eps, y_Eps, board)

    def has_eaten(self, food):
        """Has Epsilon eaten food yet?
        Epsilon has eaten when she is at the location of the food

        param:
            food: Food, the food whose location is checked if Epsilon has reached there

        return:
            True if Epsilon has reached food's location, False otherwise
        """
        return self.get_pos() == food.get_pos()

    def __str__(self):
        return '🐈'


if __name__ == '__main__':
    board_test = SquareBoard(5)

    # [case]: instantiate Epsilon
    def test_instatiate():
        # Arrange
        board_test = SquareBoard(5)

        try:
            # Act
            eps_test = Epsilon(board_test)

            # Assert
            # Epsilon has an attribute with name 'board'
            assert hasattr(eps_test, 'board'), 'Epsilon is not on any board'
            # the 'board' is an instance of BoardPiece class
            assert isinstance(getattr(eps_test, 'board'),
                              SquareBoard), 'board is not a SquareBoard'
            assert all(isinstance(_elem, int) for _elem in eps_test.get_pos())
            assert all(_elem < board_test.size for _elem in eps_test.get_pos())

            # print(str(eps_test))
            # print(eps_test.get_pos())
            # print()
        except AssertionError as assert_error:
            print(f'Failure. This occurs: {str(assert_error)}')
            print(eps_test.get_pos())

    def test_move_up(verbose=True) -> bool:
        # Arrange
        board_test = SquareBoard(5)
        eps_test = Epsilon(board_test)

        x_start, y_start = eps_test.get_pos()
        if verbose:
            print('Place Epsilon on board')
            board_test.print()

        try:
            # Act
            if verbose: print('\nMoving Epsilon up')
            eps_test.move_up()
            x_final, y_final = eps_test.get_pos()

            if verbose: board_test.print()

            # Assert
            assert x_start == x_final, 'Epsilon moves to wrong column'
            if y_start == 0:
                assert y_start == y_final, 'Epsilon moves to somewhere else not intended'
            else:
                assert y_start - 1 == y_final, 'Epsilon did not move up as intended'
            return True
        except AssertionError as err:
            print(f'Test failed: {str(err)}')
            print((x_start, y_start), (x_final, y_final))
            return False

    def test_move_in_circle(verbose=True) -> bool:
        # Arrange
        board_test = SquareBoard(5)
        eps_test = Epsilon(board_test)
        # Epsilon is positioned manually in the center
        x_start, y_start = (2, 2)
        eps_test.update_pos(x_start, y_start)

        try:
            # Act
            eps_test.move_up()
            eps_test.move_left()
            eps_test.move_down()
            eps_test.move_right()
            x_final, y_final = eps_test.get_pos()

            # Assert
            assert (x_start, y_start) == (
                x_final,
                y_final), 'Epsilon did not move back to original direction'
            return True
        except AssertionError as err:
            if verbose:
                print(f'Test failed: {str(err)}')
                print((x_start, y_start), (x_final, y_final))
            return False

    run_a_test_many_times(
        test_move_in_circle,
        10,
        test_args={"verbose": True},
    )

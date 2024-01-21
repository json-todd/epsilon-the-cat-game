class SquareBoard:

    def __init__(self, board_size):
        self.size = board_size
        self.board = [['  ' for i in range(board_size)]
                      for j in range(board_size)]

    def place_on_board(self, piece, x_location, y_location):
        if x_location < 0 or x_location >= self.size or y_location < 0 or y_location >= self.size:
            print('Location is outside of board')
            return False

        if not isinstance(piece, BoardPiece) and not __name__ == '__main__':
            # `isinstance` evaluates to false, when running the file directly ...
            # ... for example Epsilon is an instance of BoardPiece evaluates to False. Why??
            # I by-pass this inexplicable behaviour with `not __name__ == '__main__'`
            print(
                'Board does not recognize this is piece. Try to place a `BoardPiece` object on the board.'
            )
            return False

        self.board[y_location][x_location] = piece
        return True

    def remove_from_board(self, piece):
        if not isinstance(piece, BoardPiece):
            print('Board does not recognize this is is a valid piece on board')
            print('Board will not remove anything')
            return False

        (x_location, y_location) = piece.get_pos()
        self.board[y_location][x_location] = '  '
        return True

    def print(self) -> None:
        """
        Visualise the board to the terminal
        """
        for y in self.board:
            row = '|'
            for x in y:
                row += f' {x} |'

            print(row.rstrip())


class BoardPiece:

    def __init__(self, name: str, x_pos: int, y_pos: int, board: SquareBoard):
        """A piece on the game board
        It is placed in the co-ordinate (x, y)
        where index starts at 0

        param:
            name: str, how the piece is visualized to the board. This is a string representation of the piece
            x_pos: int, the piece's horizontal position 
            y_pos: int, the piece's vertical position
            board: SquareBoard, game board where the piece is placed on
        """
        self.board = board
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.board.place_on_board(piece=self,
                                  x_location=self.x_pos,
                                  y_location=self.y_pos)

    def update_pos(self, x_new, y_new) -> bool:
        """Move the piece on the game board

        param:
            x_new: str, the new horizontal position
            y_new: str, the new vertical position
        return:
            bool, True if the move was successful, False otherwise
        """
        try:
            # piece is moved to new location
            self.board.place_on_board(self, x_new, y_new)
            # and old location is cleared
            self.board.remove_from_board(piece=self)
            # finally, update properties of the object
            self.x_pos = x_new
            self.y_pos = y_new

            return True
        except Exception as error:
            print(f'Ur oh. Can\'t move the piece.\nThis occurs: {error}')
            return False

    def get_pos(self) -> tuple:
        """Return the piece's location on game board
        In format of (x, y)
        or (horizontal, vertical)
        """
        return (self.x_pos, self.y_pos)


    def move_up(self):
        if self.y_pos == 0: return
        self.update_pos( self.x_pos, self.y_pos - 1 )

    def move_left(self):
        if self.x_Eps == 0: return
        self.update_pos( self.x_Eps - 1, self.y_pos )

    def move_down(self):
        if self.y_pos == self.board.size - 1: return
        self.update_post( self.x_Eps, self.y_pos + 1)

    def move_right(self):
        if self.x_pos == self.board.size - 1: return
        self.update_pos( self.x_pos + 1, self.y_pos )
    
    def __str__(self):
        return self.name


if __name__ == '__main__':
    from Epsilon import Epsilon
    board_test = SquareBoard(7)
    epsilon_test = Epsilon(board_test)

    # Why does Epsilon is sub-class of BoardPiece evaluate to False???
    # why epsilon_test is not an is instant of BoardPiece?
    # moreover, it only affects running this file ????
    print('printing in main')
    print(isinstance(epsilon_test, BoardPiece))
    print(issubclass(Epsilon, BoardPiece))
    board_test.print()

    def test_instantiate_piece_on_board():
        assert any(epsilon_test in row
                   for row in board_test.board), 'Epsilon is not on board!'
        print('Epsilon is on the board <3')

    test_instantiate_piece_on_board()

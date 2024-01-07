class SquareBoard:

    def __init__(self, board_size):
        self.size = board_size
        self.board = [['  ' for i in range(board_size)]
                      for j in range(board_size)]

    def print(board: list) -> None:
        """
        Visualise the board to the terminal
        """
        for y in board:
            row = '|'
            for x in y:
                row += f' {x} |'

            print(row.rstrip())


class BoardPiece:

    def __init__(self, name: str, x_pos: str, y_pos: str, board):
        """A piece on the game board
        It is placed in the co-ordinate (x, y)
        where index starts at 0

        param:
            name: str, how the piece is visualized to the board. This is a string representation of the piece
            x_pos: str, the piece's horizontal position 
            y_pos: str, the piece's vertical position
            board: Board, game board where the piece is placed on
        """
        self.board = board
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

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
            self.board[y_new][x_new] = self.name
            # and old location is cleared
            self.board[self.y_pos][self.x_pos] = '  '
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

    def __str__(self):
        return self.name

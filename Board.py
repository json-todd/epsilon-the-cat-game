class SquareBoard:
    def __init__(self, board_size):
        self.size = board_size
        self.board = [
            ['  ' for i in range (board_size)] for j in range(board_size)
        ]
    
    def print(board:list) -> None:
        for y in board:
            row = '|'  
            for x in y:
                row += f' {x} |'
    
            print(row.rstrip())


    def update_obj_pos(self, object, x_obj, y_obj) -> bool:
        try:
            self.board[y_obj][x_obj] = object
            return 0
        except Exception as e:
            print(f'Ur oh. Error occurs {e}')
            return 1

from getkey import getkey, keys
from Board import SquareBoard
from Epsilon import Epsilon
from Food import Food

# Board is a square
# 7x7 board
BOARD_SIZE = 10
USER_ALLOWED_INPUT = {'w', 'a', 's', 'd', keys.UP, keys.LEFT, keys.DOWN, keys.RIGHT}
# 7x7 board for now
# TODO: suport user to decide the size. But the render to terminal may be horrible and broken, though
BOARD_SIZE = 7
QUIT_GAME_SIGNAL = 'q'
EXIT_CODE_WIN = 0
EXIT_CODE_QUIT = 1

# test case Eps & food in the same row
# test case Eps & food have same starting location
# TODO: write more test cases with pytest on presentation logic

def main():
    import subprocess   
    def user_control():
        user_command = ''
        while user_command != QUIT_GAME_SIGNAL:
            print('\nMove Epsilon with WASD or arrow keys:')
            user_command = getkey()

            if user_command not in USER_ALLOWED_INPUT:
                subprocess.call(["clear"])
                print("Woops, Epsilon doesn\'t know where to move. She stays at the same spot")
                game_board.print()
                continue
            elif user_command == 'w' or user_command == keys.UP:
                # move Epsilon upward
                Eps.move_up()
            elif user_command == 'a' or user_command == keys.LEFT:
                # move Epsilon left-ward
                Eps.move_left()
            elif user_command == 's' or user_command == keys.DOWN:
                # move Epsilon downward
                Eps.move_down()
            elif user_command == 'd' or user_command == keys.RIGHT:
                # move Epsilon right_ward:
                Eps.move_right()

            subprocess.call(["clear"])
            game_board.print()

            if Eps.has_eaten(food):
                return EXIT_CODE_WIN

        else:
            return EXIT_CODE_QUIT
    
     
    
    game_board = SquareBoard(BOARD_SIZE)
    Eps = Epsilon(game_board)
    food = Food(game_board)
    game_board.print()
    exit_code = user_control()
    if exit_code == EXIT_CODE_WIN:
        print('Epsilon ate the food.')
        print('Good job! Epsilon will give you luv.')
        print('But now, she\'s gonna sleep.')
    elif exit_code == EXIT_CODE_QUIT:
        print('You exit the game')
        print('See you next time ^^')


if __name__ == '__main__':
    main()
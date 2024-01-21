from getkey import getkey, keys
from Epsilon import Epsilon
from Food import Food
from Board import SquareBoard

# Board is a square
# 7x7 board for now
# TODO: suport user to decide the size. But the render to terminal may be horrible and broken, though
BOARD_SIZE = 7
QUIT_GAME_SIGNAL = 'q'
EXIT_CODE_WIN = 0
EXIT_CODE_QUIT = 1

USER_ALLOWED_INPUT = {'w', 'a', 's', 'd', keys.UP, keys.LEFT, keys.DOWN, keys.RIGHT, QUIT_GAME_SIGNAL}

board_game = SquareBoard(BOARD_SIZE)
Eps = Epsilon(board_game)
food = Food(board_game)

# test case Eps & food in the same row
# test case Eps & food have same starting location
# TODO: write more test cases with pytest on presentation logic

def game_thread():
    user_command = ''
    while user_command != QUIT_GAME_SIGNAL:
        board_game.print()
        print('\nMove Epsilone with [w] [a] [s] [d] or the arrow keys\nExit the game with [q]:')
        user_command = getkey()

        if user_command not in USER_ALLOWED_INPUT:
            print("Woops, Epsilon doesn\'t know where to move")
            continue

        if user_command == 'w' or user_command == keys.UP:
            Eps.move_up()
        elif user_command == 'a' or user_command == keys.LEFT:
            Eps.move_left()
        elif user_command == 's' or user_command == keys.DOWN:
            Eps.move_down()
        elif user_command == 'd' or user_command == keys.RIGHT:
            Eps.move_right()

        if not Eps.has_eaten(food): continue
        return EXIT_CODE_WIN
    else:
        return EXIT_CODE_QUIT


def main():
    exit_code = game_thread()
    if exit_code == EXIT_CODE_WIN:
        print('Epsilon ate the food.')
        print('Good job! Epsilon will give you luv.')
        print('But now, she\'s gonna sleep.')
    elif exit_code == EXIT_CODE_QUIT:
        print('You exit the game')
        print('See you next time ^^')


if __name__ == '__main__':
    main()
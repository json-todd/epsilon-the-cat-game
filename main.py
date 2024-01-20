from random import randint
from getkey import getkey, keys

# Board is a square
# 7x7 board
BOARD_SIZE = 7
BOARD = [['  ' for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
USER_ALLOWED_INPUT = {'w', 'a', 's', 'd', keys.UP, keys.LEFT, keys.DOWN, keys.RIGHT}
QUIT_GAME_SIGNAL = 'q'
EXIT_CODE_WIN = 0
EXIT_CODE_QUIT = 1


def board_print(board: list) -> None:
    for y in board:
        row = '|'
        for x in y:
            row += f' {x} |'

        print(row.rstrip())


Eps = '🐈'
food = '🥩'

x_Eps, y_Eps = [randint(0, BOARD_SIZE - 1) for i in range(2)]
x_food, y_food = [randint(0, BOARD_SIZE - 1) for i in range(2)]

# test case Eps & food in the same row
# TODO: write more test cases with pytest on presentation logic
# x_Eps, y_Eps = [0, 0]
# x_food, y_food= [6, 0]

BOARD[y_Eps][x_Eps] = f'{Eps}'
BOARD[y_food][x_food] = f'{food}'

print(Eps, (x_Eps, y_Eps))
print(food, (x_food, y_food))


def update_Epsilon_pos_on_board(x_Eps, y_Eps) -> bool:
    try:
        BOARD[y_Eps][x_Eps] = f'{Eps}'
        return 0
    except Exception as e:
        print(f'Ur oh. Error occurs {e}')
        return 1


def has_Epsilon_eaten() -> bool:
    global x_Eps, y_Eps, x_food, y_food
    return (x_Eps, y_Eps) == (x_food, y_food)


def user_control():
    global x_Eps, y_Eps

    user_command = ''
    while user_command != QUIT_GAME_SIGNAL:
        old_x_Eps, old_y_Eps = x_Eps, y_Eps
        print('\nMove Epsilone with [W] [A] [S] [D]:')
        user_command = getkey()

        if user_command not in USER_ALLOWED_INPUT:
            print("Woops, Epsilon doesn\'t know where to move")
            continue

        if user_command == 'w' or user_command == keys.UP:
            # move Epsilon upward
            if y_Eps == 0:
                board_print(BOARD)
                continue
            y_Eps -= 1
        elif user_command == 'a' or user_command == keys.LEFT:
            # move Epsilon left-ward
            if x_Eps == 0:
                board_print(BOARD)
                continue
            x_Eps -= 1
        elif user_command == 's' or user_command == keys.DOWN:
            # move Epsilon downward
            if y_Eps == BOARD_SIZE - 1:
                board_print(BOARD)
                continue
            y_Eps += 1
        elif user_command == 'd' or user_command == keys.RIGHT:
            # move Epsilon right_ward:
            if x_Eps == BOARD_SIZE - 1:
                board_print(BOARD)
                continue
            x_Eps += 1

        update_Epsilon_pos_on_board(x_Eps, y_Eps)
        # forget the Epslon previous position
        BOARD[old_y_Eps][old_x_Eps] = '  '
        board_print(BOARD)

        if not has_Epsilon_eaten(): continue
        return EXIT_CODE_WIN

    else:
        return EXIT_CODE_QUIT


def main():
    # subprocess.call(["clear"])
    board_print(BOARD)
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

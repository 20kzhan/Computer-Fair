# *ominous music starts playing*

from random import randint

X_O_STR = ['   ', ' O ', ' X ']
DIVIDER_STR = ['-' * 11 + ' ' * 8 + '-' * 11, '-' * 11 + ' ' * 8 + '-' * 11, '']
HORIZONTAL_DIVIDER = ['|', '|', ' ' * 8]

BOARD_ROW = 5
BOARD_COL = 5


def get_stats(board2d):
    """Returns various statistics about the board."""

    ncorners = 0
    nsides = 0
    ncenter = 0

    # Calculate the number of corners occupied
    if board2d[0][0] == 1:
        ncorners += 1
    if board2d[0][2] == 1:
        ncorners += 1
    if board2d[0][2] == 1:
        ncorners += 1
    if board2d[2][0] == 1:
        ncorners += 1
    if board2d[2][2] == 1:
        ncorners += 1

    # Calculate the number of sides occupied
    if board2d[0][1] == 1:
        nsides += 1
    if board2d[1][0] == 1:
        nsides += 1
    if board2d[1][2] == 1:
        nsides += 1
    if board2d[2][1] == 1:
        nsides += 1

    # ncenter is 1 if the center of the board is occupied
    if board2d[1][1] == 1:
        ncenter += 1

    return ncorners, nsides, ncenter


def block(board_2d):
    for each_row in board_2d:
        for i in range(len(each_row)):
            if each_row[i] == 0:
                each_row[i] = 1
                if check_game_over(board_2d)[0]:
                    each_row[i] = 2
                    return True
                else:
                    each_row[i] = 0
    return False


def finish_board(board_2d):
    for each_row in board_2d:
        for i in range(len(each_row)):
            if each_row[i] == 0:
                each_row[i] = 2
                if check_game_over(board_2d)[0]:
                    return True
                else:
                    each_row[i] = 0
    return False


def ai_next_move(board_2d):
    turns_taken = 0
    for each_row in board_2d:
        for i in range(len(each_row)):
            if each_row[i] != 0:
                turns_taken += 1
    if finish_board(board_2d):
        return
    elif block(board_2d):
        return
    elif turns_taken == 1:
        if get_stats(board_2d)[2] == 0:
            board_2d[1][1] = 2
        else:
            board_2d[0][0] = 2
        return
    elif turns_taken == 3:
        if get_stats(board_2d)[0] == 1 and get_stats(board_2d)[1] == 1:
            if board_2d[2][1] == 1 or board_2d[1][2] == 1:
                board_2d[2][2] = 2
                return
            else:
                board_2d[0][0] = 2
                return
        elif get_stats(board_2d)[0] == 2:
            board_2d[0][1] = 2
            return
        elif get_stats(board_2d)[1] == 2:
            if board_2d[2][1] == board_2d[1][2] == 1:
                board_2d[2][2] = 2
            else:
                board_2d[0][0] = 2
            return
        elif get_stats(board_2d)[0] == 1 and get_stats(board_2d)[2] == 1:
            board_2d[0][2] = 2
            return
    else:
        while True:
            row = randint(0, 2)
            col = randint(0, 2)
            if board_2d[row][col] == 0:
                board_2d[row][col] = 2
                return


def print_board(board_2d):
    """Prints the board to the screen"""

    print("board".center(11), end=' ' * 8)
    print("choices".center(11))
    for n, each_row in enumerate(board_2d):
        for i in range(len(each_row)):
            print(X_O_STR[each_row[i]], end='')
            print(HORIZONTAL_DIVIDER[i], end='')

        for i in range(len(each_row)):
            print(' ' + str(i + n * 3 + 1) + ' ' if each_row[i] == 0 else ' . ', end='')
            print(HORIZONTAL_DIVIDER[i], end='')

        print()
        print(DIVIDER_STR[n])


def check_game_over(board_2d):
    """Returns whether the game is over, if it is say who won as well."""

    temp_list = []
    for i in range(len(board_2d[0])):
        for each_row in board_2d:
            temp_list.append(each_row[i])
        if len(list(set(temp_list))) == 1 and temp_list[0] == 1:
            return True, 'O'
        elif len(list(set(temp_list))) == 1 and temp_list[0] == 2:
            return True, 'X'
        temp_list = []
    for i in range(len(board_2d[0])):
        for each_row in board_2d:
            if len(list(set(each_row))) == 1 and each_row[0] == 1:
                return True, 'O'
            elif len(list(set(each_row))) == 1 and each_row[0] == 2:
                return True, 'X'
    cross1sum = []
    cross0sum = []
    for i in range(len(board_2d)):
        cross1sum.append(board_2d[(len(board_2d[0]) - 1) - i][i])
        cross0sum.append(board_2d[i][i])
    if len(list(set(cross1sum))) == 1 and cross1sum[0] == 1:
        return True, 'O'
    elif len(list(set(cross1sum))) == 1 and cross1sum[0] == 2:
        return True, 'X'
    if len(list(set(cross0sum))) == 1 and cross0sum[0] == 1:
        return True, 'O'
    elif len(list(set(cross0sum))) == 1 and cross0sum[0] == 2:
        return True, 'X'
    for each_row in board_2d:
        if each_row.count(0) != 0:
            return False, 0
    return True, 0


def update_board(board_2d, row, col, change_to):
    """Update the board with the correct positions."""

    if board_2d[row][col] == 0:
        if change_to == -1:
            board_2d[row][col] = 2
        elif change_to == 1:
            board_2d[row][col] = 1


def check_pos_clear(board_2d, row, col):
    if board_2d[row][col] == 0:
        return True
    else:
        return False


def play_game():
    """Starts the game."""
    while True:
        game_board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

        print_board(game_board)

        last_turn_taken = 1

        while True:
            if last_turn_taken == -1:
                ai_next_move(game_board)
                print_board(game_board)
                if check_game_over(game_board)[0] is True and check_game_over(game_board)[1] != 0:
                    print("                                ")
                    print('              ' + str(check_game_over(game_board)[1]) + ' Wins!' + '              ')
                    return
                elif check_game_over(game_board)[0]:
                    print("                                ")
                    print("         It's a tie!         ")
                    return
                last_turn_taken *= -1

            if last_turn_taken == 1:
                while True:
                    c = input("O's turn, please make your move: ")
                    if c == '1' and check_pos_clear(game_board, 0, 0):
                        update_board(game_board, 0, 0, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '2' and check_pos_clear(game_board, 0, 1):
                        update_board(game_board, 0, 1, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '3' and check_pos_clear(game_board, 0, 2):
                        update_board(game_board, 0, 2, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '4' and check_pos_clear(game_board, 1, 0):
                        update_board(game_board, 1, 0, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '5' and check_pos_clear(game_board, 1, 1):
                        update_board(game_board, 1, 1, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '6' and check_pos_clear(game_board, 1, 2):
                        update_board(game_board, 1, 2, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '7' and check_pos_clear(game_board, 2, 0):
                        update_board(game_board, 2, 0, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '8' and check_pos_clear(game_board, 2, 1):
                        update_board(game_board, 2, 1, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    elif c == '9' and check_pos_clear(game_board, 2, 2):
                        update_board(game_board, 2, 2, last_turn_taken)
                        last_turn_taken *= -1
                        break
                    else:
                        print("\nError: invalid move or spot is already taken!\n")
                        print_board(game_board)

                print()
            if check_game_over(game_board)[0] and check_game_over(game_board)[1] != 0:
                print_board(game_board)
                print("                                ")
                print('              ' + str(check_game_over(game_board)[1]) + ' Wins!' + '              ')
                return
            elif check_game_over(game_board)[0]:
                print_board(game_board)
                print("                                ")
                print("            It's a tie!         ")
                return


if __name__ == '__main__':
    play_game()

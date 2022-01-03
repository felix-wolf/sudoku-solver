import numpy as np


def solve_sudoku():
    board = np.array([
        np.array([3, 0, 6, 5, 0, 8, 4, 0, 0]),
        np.array([5, 2, 0, 0, 0, 0, 0, 0, 0]),
        np.array([0, 8, 7, 0, 0, 0, 0, 3, 1]),
        np.array([0, 0, 3, 0, 1, 0, 0, 8, 0]),
        np.array([9, 0, 0, 8, 6, 3, 0, 0, 5]),
        np.array([0, 5, 0, 0, 9, 0, 6, 0, 0]),
        np.array([1, 3, 0, 0, 0, 0, 2, 5, 0]),
        np.array([0, 0, 0, 0, 0, 0, 0, 7, 4]),
        np.array([0, 0, 5, 2, 0, 6, 3, 0, 0])
    ])

    board = np.array([
        np.array([0, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([0, 0, 0, 0, 0, 3, 0, 8, 5]),
        np.array([0, 0, 1, 0, 2, 0, 0, 0, 0]),
        np.array([0, 0, 0, 5, 0, 7, 0, 0, 0]),
        np.array([0, 0, 4, 0, 0, 0, 1, 0, 0]),
        np.array([0, 9, 0, 0, 0, 0, 0, 0, 0]),
        np.array([5, 0, 0, 0, 0, 0, 0, 7, 3]),
        np.array([0, 0, 2, 0, 1, 0, 0, 0, 0]),
        np.array([0, 0, 0, 0, 4, 0, 0, 0, 9])
    ])

    print(f"solve this here:\n{board}")
    solve_sudoku_bt(board)


def solve_sudoku_bt(board: np.array):
    if is_solution(board):
        print(f"solution found:\n{board}")
        return True
    else:
        next_field, possible_values = get_next_field(board)
        for value in possible_values:
            board[next_field] = value
            rtn = solve_sudoku_bt(board)
            if rtn:
                return True
            board[next_field] = 0  # unmake move


def get_next_field(board: np.array):
    # get field that is most constrained
    current_min = 9
    available_numbers_for_field = np.array
    field_index = None

    # for every field in board
    for index, element in np.ndenumerate(board):
        if element == 0:
            available_numbers = calculate_constraints_for_field(board, index)
            if len(available_numbers) < current_min:
                current_min = len(available_numbers)
                field_index = index
                available_numbers_for_field = available_numbers
    return field_index, available_numbers_for_field


def calculate_constraints_for_field(board: np.array, index):
    """returns the list of possible values"""
    values = np.arange(1, 10)

    # check row
    values = np.setdiff1d(values, board[index[0]])

    # check column
    values = np.setdiff1d(values, board.copy().transpose()[index[1]])

    # check square
    surrounding_fields = get_surrounding_values(board, index)

    values = np.setdiff1d(values, surrounding_fields)

    return values


def get_surrounding_values(board: np.array, index):
    vertical = index[0] // 3
    horizontal = index[1] // 3
    return np.array([
        board[3 * vertical + 0][3 * horizontal + 0],
        board[3 * vertical + 1][3 * horizontal + 0],
        board[3 * vertical + 2][3 * horizontal + 0],
        board[3 * vertical + 0][3 * horizontal + 1],
        board[3 * vertical + 1][3 * horizontal + 1],
        board[3 * vertical + 2][3 * horizontal + 1],
        board[3 * vertical + 0][3 * horizontal + 2],
        board[3 * vertical + 1][3 * horizontal + 2],
        board[3 * vertical + 2][3 * horizontal + 2],
    ])


def is_solution(board):
    for index, value in np.ndenumerate(board):
        if value == 0:
            return False
    return True


if __name__ == "__main__":
    solve_sudoku()

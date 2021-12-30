import numpy as np


def solve_sudoku():
    board = np.array([
        np.array([1, 4, 5, 2, 3, 6, 7, 8, 9]),
        np.array([2, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([3, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([4, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([5, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([6, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([7, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([8, 0, 0, 0, 0, 0, 0, 0, 0]),
        np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    ])
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
    # print(array)
    # print(array.size)
    print(f"solve this here:\n{board}")
    solution = solve_sudoku_bt(board)
    if solution:
        print("solution found")
    else:
        print("no solution found :(")


def solve_sudoku_bt(board: np.array):
    if is_solution(board):
        return True
    else:
        next_field, possible_values = get_next_field(board)
        if len(possible_values) == 0:
            return False
        for value in possible_values:
            board[next_field] = value
            solve_sudoku_bt(board)
            board[next_field] = 0
        return False


def get_next_field(board: np.array):
    # candidates = np.arange(0, 10)
    # get field with the least constraint
    current_min = 8 + 8 + 8
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
    surrounding_fields = np.array([0, 0])

    if index[0] > 0 and index[1] > 0:
        surrounding_fields = np.append(
            surrounding_fields, [
                board[index[0] - 1][index[1] - 1],
                board[index[0] - 1][index[1] + 0],
                board[index[0] - 0][index[1] - 1]
            ]
        )

    if index[0] > 0 and index[1] < 8:
        surrounding_fields = np.append(
            surrounding_fields, [
                board[index[0] - 1][index[1] + 1]
            ]
        )

    if index[1] < 8:
        surrounding_fields = np.append(
            surrounding_fields, [
                board[index[0]][index[1] + 1]
            ]
        )

    if index[0] < 8 and index[1] > 0:
        surrounding_fields = np.append(
            surrounding_fields, [
                board[index[0] + 1][index[1] - 1],
                board[index[0] + 1][index[1] + 0],
            ]
        )
    if index[0] < 8 and index[1] < 8:
        surrounding_fields = np.append(
            surrounding_fields, [
                board[index[0] + 1][index[1] + 1]
            ]
        )

    values = np.setdiff1d(values, surrounding_fields)

    return values


def is_solution(board):
    print(board)
    for index, value in np.ndenumerate(board):
        if value == 0:
            return False
    return True


if __name__ == "__main__":
    solve_sudoku()

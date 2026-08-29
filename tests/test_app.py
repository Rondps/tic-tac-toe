from app import check_winner, bot_move, reset_game

def test_check_winner_horizontal_x():
    board = [
        ['X', 'X', 'X'],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert check_winner(board) == 'X'

def test_check_winner_horizontal_o():
    board = [
        ['O', 'O', 'O'],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert check_winner(board) == 'O'

def test_check_winner_vertical_x():
    board = [
        ['X', ' ', ' '],
        ['X', ' ', ' '],
        ['X', ' ', ' ']
    ]
    assert check_winner(board) == 'X'

def test_check_winner_vertical_o():
    board = [
        [' ', 'O', ' '],
        [' ', 'O', ' '],
        [' ', 'O', ' ']
    ]
    assert check_winner(board) == 'O'

def test_check_winner_diagonal_x():
    board = [
        ['X', ' ', ' '],
        [' ', 'X', ' '],
        [' ', ' ', 'X']
    ]
    assert check_winner(board) == 'X'

def test_check_winner_diagonal_o():
    board = [
        [' ', ' ', 'O'],
        [' ', 'O', ' '],
        ['O', ' ', ' ']
    ]
    assert check_winner(board) == 'O'

def test_check_winner_draw():
    board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert check_winner(board) == 'Draw'

def test_check_winner_incomplete():
    board = [
        ['X', 'O', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert check_winner(board) is None

def test_bot_move():
    board = [
        ['X', ' ', ' '],
        [' ', 'O', ' '],
        [' ', ' ', ' ']
    ]
    result = bot_move(board)
    assert result in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]

def test_bot_move_no_empty():
    board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert bot_move(board) is None

def test_reset_game():
    board = [
        ['X', 'O', 'X'],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    new_board = reset_game()
    assert new_board == [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
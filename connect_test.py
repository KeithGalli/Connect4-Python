

import unittest

# The winning_move function that checks for horizontal wins
def winning_move(board, piece):
    for c in range(len(board[0]) - 3):  # COLUMN_COUNT-3 equivalent
        for r in range(len(board)):  # ROW_COUNT equivalent
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    return False

# Tests for winning_move
class TestConnectFour(unittest.TestCase):

    def test_horizontal_win_first_row(self):
        board = [
            ["X", "X", "X", "X"],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]
        ]
        self.assertTrue(winning_move(board, "X"))

    def test_horizontal_win_second_row(self):
        board = [
            [" ", " ", " ", " "],
            ["X", "X", "X", "X"],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]
        ]
        self.assertTrue(winning_move(board, "X"))

    def test_no_horizontal_win(self):
        board = [
            ["X", "O", "X", " "],
            ["O", "X", "O", " "],
            ["X", "O", "X", " "],
            ["O", "X", "O", "X"]
        ]
        self.assertFalse(winning_move(board, "X"))
        self.assertFalse(winning_move(board, "O"))

    def test_horizontal_win_O(self):
        board = [
            ["O", "O", "O", "O"],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "]
        ]
        self.assertTrue(winning_move(board, "O"))

    def test_horizontal_win_with_spaces(self):
        board = [
            [" ", " ", "X", "X"],
            [" ", " ", "X", "X"],
            [" ", " ", "X", "X"],
            [" ", " ", "X", "X"]
        ]
        self.assertTrue(winning_move(board, "X"))

if __name__ == "__main__":
    unittest.main()

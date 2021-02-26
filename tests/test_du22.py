import unittest
from du12 import check_sudoku 

class DruhaUloha(unittest.TestCase):
    def test_check_sudoku(self):
        """
        Test sudoku
        """
        self.assertEqual(False, check_sudoku([1, 2, 3]))
        self.assertEqual(False, check_sudoku([2, 8, 9, 456]))
        self.assertEqual(True, check_sudoku([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertEqual(False, check_sudoku([1, 1, 4, 4, 5, 6, 7, 8, 9]))

    def test_check_sudoku_2(self):
        """
        Test sudoku 2
        """
        self.assertEqual(False, check_sudoku([1, 2, 3, 4, 4, 5, 6, 7, 8, 9,]))

    def test_check_sudoku_3(self):
        """
        Test sudoku 3 
        """
        self.assertEqual(False, check_sudoku([1, 3, 5, 4, 2, 7, 6, 9, 8]))

    def test_check_sudoku_4(self):
        """
        Test sudoku is bool
        """
        self.assertEqual(check_sudoku([1, 2, 3, 4]), bool)
        
    def test_sudoku_is_correct_length(self):
        """
        Test sudoku must be 9 numbers
        """
        self.assertEqual(False, check_sudoku([20, 25]))
        self.assertEqual(True, check_sudoku([1, 2, 3, 4, 5, 6, 7, 8, 9]))



if __name__ == '__main__':
    unittest.main()

    
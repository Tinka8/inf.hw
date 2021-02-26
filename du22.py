def check_sudoku(row):
    
    return sum(set(row)) == 45 and len(row) == 9

print(check_sudoku([1, 2, 3]))
print(check_sudoku([2, 8, 9, 456]))
print(check_sudoku([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(check_sudoku([1, 1, 4, 4, 5, 6, 7, 8, 9]))
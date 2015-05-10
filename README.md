# Sudoku
It's a solver and a generator of full or partial compiled Sudokus.
Examples:
```
from sudoku import get_random_sudoku,solve_sudoku

#generate a single random classic full compiled Sudoku
sudoku=get_random_sudoku()

#generate a single random classic Sudoku with 10 removed cell
sudoku=get_random_sudoku(10)

#solve a sudoku
solved=solve_sudoku(sudoku)
```


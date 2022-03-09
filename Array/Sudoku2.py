#Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid all contain all of the numbers from 1 to 9 one time.

#Implement an algorithm that will check whether the given grid of numbers represents a valid Sudoku puzzle according to the layout rules described above. Note that the puzzle represented by grid does not have to be solvable.



def solution(grid):
    rows = grid
    cols = zip(*grid)
    subs = []

    for i in range(0,7,3):
        for j in range(0,7,3):
            subs.append([grid[r][c] for r in range(i,i+3) for c in range(j,j+3)])

    def isvalid(arr):
        nums = [x for x in arr if str.isdigit(x)]
        return len(nums) == len(set(nums))

    return all([
        all(map(isvalid, rows)),
        all(map(isvalid, cols)),
        all(map(isvalid, subs))
    ])

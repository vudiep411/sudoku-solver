import random

def print_sudoku(state):
    border = "------+------+------"
    rows = [state[i:i+9] for i in range(0,81,9)]
    for i,row in enumerate(rows):
        if i % 3 == 0:
            print(border)
        three = [row[i:i+3] for i in range(0,9,3)]
        print(" |".join(
            " ".join(str(x or "_") for x in one)
            for one in three
        ))
    print(border)

# Generate a random solution from a Sudoku problem
def init_solution_row(problem):
    solution = []
    for i in range(0, 81, 9):
        row = problem[i:i+9]
        p = [n for n in range(1,10) if n not in row]
        random.shuffle(p)
        solution.extend([n or p.pop() for n in row])
    return solution

# Calculate coordinate in 1D array
def coord(row, col):
    return row*9 + col
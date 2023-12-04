from lib.simanneal import Annealer
import random
from utils.functions import init_solution_row, coord

class Sudoku(Annealer):
    def __init__(self, problem):
        self.problem = problem
        state = init_solution_row(problem)
        super().__init__(state)
        
    def move(self):
        """randomly swap two cells in a random row"""
        initial_e = self.energy()
        row = random.randrange(9)
        coords = range(9*row, 9*(row+1))    # Getting random range for a row
        n1, n2 = random.sample([n for n in coords if self.problem[n] == 0], 2)  # coords is range(random_val1, random_val2)
        self.state[n1], self.state[n2] = self.state[n2], self.state[n1]     # swapping
        return self.energy() - initial_e

    def column_score(self, col):
        val_in_col = set(self.state[coord(i, col)] for i in range(9))
        violations = -len(val_in_col)
        return violations

    def square_score(self, row, col):
        val_in_square = set(self.state[coord(3*row+i, 3*col+j)] for i in range(3) for j in range(3))
        violations = -len(val_in_square)
        return violations

    def energy(self):
        """calculate the number of violations: assume all rows are OK"""
        score = sum(self.column_score(n) for n in range(9)) + sum(self.square_score(n,m) for n in range(3) for m in range(3))
        if score == -162:
            self.user_exit = True
        return score

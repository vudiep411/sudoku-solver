# CPSC 481 AI project
I'm using simulated annealing to demonstrate how it can be used to solve a sudoku.

## Quick overview
I will be using simulated annealing to solve a sudoku puzzle with the following step:

  1. Generate an initial state with random numbers filled in
  2. Randomly swap two cells in a random row
  3. Calculate the energy of the state to find a global minimal
  4. Run through the simulated annealing function

## How to run
For dfs algorithm

```
python3 sudoku_dfs.py
```

For simulated annealing

```
python3 main.py
```

## Library
* Open source library [simanneal](https://github.com/perrygeo/simanneal)


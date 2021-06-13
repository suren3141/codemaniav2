## Where's the clue

### Description

A competitor in a reality show is required to solve a cross word puzzle based on the clues ge gets.
He needs $n$ clues to solve the puzzle and these clues appear at different times based on two given integers $x$ and $y$.
At a given minute $t$ a new clue appears if $t$ is either a multiple of $x$ or a multiple of $y$.
The competitor needs to know the minimum time it takes to receive all $n$ clues beforehand. Can you help him?

**Problem setter** : [Dr. Dileepa Fernando](https://sltc.ac.lk/staff/profile/Dileepa_Fernando)

### Input Format

The first line contains an integer $T$ denoting the number of test cases.

Each of the following $T$ lines contain 3 integers $n$, $x$ and $y$, where $n$ denotes the number of clues required and
the clues appear at multiples of either $x$ or $y$.

### Constraints

$1 \leq T \leq 10^5$

$1 \leq n \leq 10^9$

$2 \leq x, y \leq 10^3$

### Output Format

For each test case, output the positive integer $t_n$ which is the minimum waiting time for all $n$ clues.


## General Note :

- Problems may not be rendered properly in github as markdown does not support latex equations. So, click [here](https://www.hackerrank.com/contests/codemania-v2) to view them with better render in hackerrank.
- Refer [solve.py](solve.py) for the optimal solution.
- Refer [naive.py](naive.py) for the optimal solution.
- Refer input and output folders for the input and the corresponding output.
- Refer [SAMPLE.txt](SAMPLE.txt) for a sample test case.



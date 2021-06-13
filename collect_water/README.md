## Collect Water

### Description

You are given $n$ non-negative integers representing an elevation map where the width of each bar is 1.

Compute how much water it can trap after raining. (refer figure)

Since the answer can be a huge number, return the answer modulo $10^9 + 7$.

![collect water](https://s3.amazonaws.com/hr-assets/0/1623351504-4e63978256-image2.png)

Problem Setter : [Thilina Herath](https://sltc.ac.lk/staff/profile/Thilina_Herath)


### Input Format

The first line contains an integer $T$ denoting the number of test cases.

The next $2T$ lines describe the test cases.

Each test case is described by 2 line:

- The first line contains an integer $n$ denoting the number of integers.

- The next line contains $n$ space separated integers denoting the elevation $e_i$  ($1 \leq i \leq n$).


### Constraints

$1 \leq T \leq 10$

$1 \leq n \leq 10^5$

$0 \leq e_i \leq 10^9$

### Output Format

For each test case, print a single integer which represents the amount of water than can be trapped.


## General Note :

- Problems may not be rendered properly in github as markdown does not support latex equations. So, click [here](https://www.hackerrank.com/contests/codemania-v2) to view them with better render in hackerrank.
- Refer [solve.py](solve.py) for the optimal solution.
- Refer [naive.py](naive.py) for the optimal solution.
- Refer input and output folders for the input and the corresponding output.
- Refer [SAMPLE.txt](SAMPLE.txt) for a sample test case.


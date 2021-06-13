## Publish or Perish!

### Description

The head of one of the departments (HOD) at SLTC wants to rank the researchers in the university based on their h-index.

[h-index](https://en.wikipedia.org/wiki/H-index) is a metric used to quantize the amount of citations received by an author.
The h-index is defined as the maximum value of $h$ such that the given author has published at least $h$ papers that have each been cited at least $h$ times.

Given the number of publications, their authors and the citation count, can you help the HOD find the h-index of the authors.


### Input Format

The first line contains two integers $N$ and $Q$ represeting the number of publications and the number of queries respectively.

The next line contains $N$ space separated integers, $k_1 k_2 \ldots k_i \ldots k_N$, where $k_i$ is the number of authors in the $i$th publication. ($1 \leq i \leq N$)

Each of the next $N$ lines contain $k_i + 1$ number of space separated values, where the first value represents the number of citations of $c_i$ of the $i$th publication
and each of the following $k_i$ values contain the name of the authors $a_{i, j}$ separated by spaces. $a_{i, j} is the $j$th author of the $i$th publication. ($1 \leq j \leq k_i$)

Each of the next $Q$ lines contain the name of an author.


### Constraints

$1 \leq N \leq 10^3$

$1 \leq Q \leq 10^3$

$0 \leq c_i \leq 10^9$

$0 \leq k_i \leq 10^3$

$1 \leq len(a_{i, j}) \leq 10$

The same authors name will not be repeated in a single publication.

The h-index of one author will not be queried twice.


### Output Format

For each query, print the h-index of the given author.


## General Note :

- Problems may not be rendered properly in github as markdown does not support latex equations. So, click [here](https://www.hackerrank.com/contests/codemania-v2) to view them with better render in hackerrank.
- Refer [solve.py](solve.py) for the optimal solution.
- Refer input and output folders for the input and the corresponding output.
- Refer [SAMPLE.txt](SAMPLE.txt) for a sample test case.




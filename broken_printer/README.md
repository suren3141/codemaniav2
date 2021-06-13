## Broken printer

### Description

Nero the printshop owner needs to print a book numbered from $1$ ($1,2,3…$).
To print the numbers, the printer has a counter function which counts the pages.
However, the printer has an error and instead of counting the number of pages, it counts the number of digits required to print.

For instance to print 5 pages, you'll have digits [1, 2, 3, 4, 5] and thus the counter function outputs $5$
However, to print 11 pages, you'll have digits [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and the counter function outputs $13$.

Nero needs to find the number of pages so that he can supply the papers.
Can you help nero with a debugging function which finds the actual number of pages from the output of the counter function.

### Input Format

The only input line contains a positive integer $D$ indicating the number of digits contained in page numbers.

### Constraints

$1 \leq D \leq 10^9$


### Output Format

Output a positive integer $N$ indicating the number of pages in the book. Output -1 if the number of digits does not form a valid page count.

## General Note :

- Problems may not be rendered properly in github as markdown does not support latex equations. So, click [here](https://www.hackerrank.com/contests/codemania-v2) to view them with better render in hackerrank.
- Refer [solve.py](solve.py) for the optimal solution.
- Refer [naive.py](naive.py) for the optimal solution.
- Refer input and output folders for the input and the corresponding output.
- Refer [SAMPLE.txt](SAMPLE.txt) for a sample test case.


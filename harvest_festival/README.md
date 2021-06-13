## Harvest festival

### Description

Leslie wants to Jerry to build a stage for the harvest festival. For this purpose she gives jerry multiple pillars. The pillars have different areas ($A$), and different strengths (determined by maximum exertable pressure $P$). Jerry is worried about the strength of the stage built using these pillars, and as such wants your help.

You are required to build a stage by using **at most $k$ number of pillars**. As pressure is evenly distributed, the maximum force that the stage can withstand depends on the pillar with the lowest strength.

Calculate the maximum amount of force that the stage can withstand. Since the answer can be a huge number, return it **modulo $10^9 + 7$**.

*Hints :*

- The relationship between force, pressure and area is given by $F = P \times A$.

- If you use $l$ pillars with areas $[A_1, A_2, \ldots, A_l]$ and maximum pressure $[P_1, P_2, \ldots, P_l]$, then the maximum force that can be exerted is given by $F_{max} = \sum_{i=1}^l {A_i} \times \min_{i=1..l}{P_i}$



### Input Format

The first line contains an integer $T$ denoting the number of test cases.

The following $3T$ lines describe the test cases as follows:

- Each test case is described by $3$ lines

- The first line contains two integers $n$ and $k$ denoting the number of pillars, and the number of maximum pillars that can be used for a stage

- The next line contains $n$ space separated integers denoting the areas of the pillar : $A_i$.

- The next line contains $n$ space separated integers denoting the maximum exertable pressure $P_i$.


### Constraints

$1 /leq T /leq 10$

$1 /leq k /leq n /leq 10^5$

$1 /leq A_i /leq 10^9$

$1 /leq P_i /leq 10^9$


### Output Format

For each test case, print a single integer which represents the maximum force that can be exerted ($F_{max}$)




Captain Haddock wants to recruit the most strongest fisherman to his sail boat. For this purpose he places them on an island and asks them to throw a fishing net with their full strength so that they can catch as many fish as possible.

Fishes are located randomly around the island. The fishing net is square shaped, and a fish gets caught in the net if its within the reach of the net. In a 2D cartesian plane, the island is located at $(0, 0)$. Given the positions of the fish in the 2D plane and the strength of the person (given by the distance to which he could throw the net), find the number of fish that could be caught by each fisherman.


Input Format

The first line contains two space separated integers, $n$ and $m$, where $n$ denotes the the number of fish and $m$ denotes the number of fishermen.

Each of the $n$ following lines contain 2 space separated integers $x_i$ and $y_i$, which donate the 2D location of the fish $i$ ($1 \leq i \leq n$).

Each of the $m$ following lines contain a single integer $d_j$, which represents the distance to which the $j$th fisherman can throw the net ($1 \leq j \leq n$).

**Note that the fishing net is square shaped and a fish is caught if $x_i \leq d_j$ and $y_i \leq d_j$**


Constraints

$1 \leq n \leq 10^5$

$1 \leq m \leq 10^5$

$-10^9 \leq x_i, y_i \leq 10^9$

$0 \leq d_j \leq 10^9$



Output Format

For each fisherman $j$, output the number of fish that he can catch.

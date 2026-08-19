# TREECNT7

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Tree Counting

You are given an array $A$ containing $N$ integers such that $\sum A_i = N$.

For a given labelled tree $T$ on $N$ nodes, you can do the following operation multiple times:

- Choose $2$ nodes $u$ and $v$ such that $dist^{\dagger}(u, v) = 2$, and then update $A_u \leftarrow A_u - 1$ and $A_v \leftarrow A_v + 1$.

A tree is said to be good if it is possible to obtain $A = [1, 1, \ldots, 1]$ using the above operation multiple times (possibly $0$).

Count the number of good trees. Since the answer may be large, find it modulo $998244353$.

$^{\dagger} dist(u, v)$ represents the number of edges on the unique simple path between nodes $u$ and $v$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output the number of good trees modulo $998244353$.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 400$
- $0 \le A_i \le N$
- $\sum A_i = N$
- The sum of $N^2$ does not exceed $400^2$.
### Sample 1:
Input
Output

```
3
4
1 1 1 1
3
1 0 2
3
3 0 0

```

```
16
1
0
```

### Explanation:

 **Test Case 1:**  Every tree is valid, since the array is already all $1$s. By cayley's formula, we know there are $4^2$ labelled trees of size $4$.

 **Test Case 2:**  Only the tree with the set of edges $\{(1, 2), (1, 3)\}$ is valid.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T16:07:17.327Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

}

```

---

[View on CodeChef](https://www.codechef.com/problems/TREECNT7)
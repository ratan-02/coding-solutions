# MODSUB

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Modify and Subtract

A given array $A$ is said to be good if it can be transformed into $[0, 0, \ldots, 0]$ with the use of the following operation used multiple times (possibly $0$):

- Choose an index $i$ ($1 \le i < N$) and subtract $1$ from each of $A_i$ and $A_{i + 1}$.

You are given an array $A$ of $N$ integers.

Count the number of indices $i$ ($1 \le i \le N$) such that there exists a valid integer $X$ where after changing $A_i = X$, the array $A$ is good.

Note that you may choose $X = A_i$ itself, and not change the array at all.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the number of indices $i$ such that there exists valid $X$.

### Constraints
- $1 \le T \le 10^4$
- $2 \le N \le 2 \cdot 10^5$
- $0 \le A_i \le 10^9$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
### Sample 1:
Input
Output

```
3
3
1 1 1
5
3 4 0 4 3
2
3 3

```

```
3
1
2
```

### Explanation:

 **Test Case 1:**  We can do the following changes for each index :

- $i = 1$ : Update $A_1 = 0$. The array $[0, 1, 1]$ is good.
- $i = 2$ : Update $A_2 = 2$. The array $[1, 2, 1]$ is good.
- $i = 3$ : Update $A_3 = 0$. The array $[1, 1, 0]$ is good.

 **Test Case 2:**  The only valid index is $i = 3$, and that has to be changed to $2$. The array is $[3, 4, 2, 4, 3]$ which is good.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T16:04:23.308Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

}

```

---

[View on CodeChef](https://www.codechef.com/problems/MODSUB)
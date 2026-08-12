# BINSPLT

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Binary Split

You are given a  **binary**  string $S$ of length $N$.

You can modify it using the following operation:

- Choose an index $i$ ($1 \le i \lt |S|$) such that $S_i \ne S_{i+1}$. Here, $|S|$ denotes the current length of $S$.
- Split $S$ into two parts: one being the prefix till index $i$ and the other being the remaining suffix.
- Then, you must discard one of these two parts and keep the other one. The part you keep becomes the new value of $S$. However, there is one condition: the part you keep must contain at least one occurrence of both $0$ and $1$, i.e. it cannot consist of only a single type of character. If both parts contain both characters, you can freely choose which one to keep. If neither part contains both characters, you are not allowed to choose this index $i$ for an operation.

You are allowed to perform the given operation however many times you like (including zero times).

Find the  *lexicographically minimum* $^\dagger$ possible final value of string $S$ after the operations.

$^\dagger$We say a binary string $P$ is lexicographically smaller than another binary string $Q$ if and only if:

- $|P| \lt |Q|$ and $P$ is a prefix of $Q$, or
- There exists an index $i$ ($1 \le i \le \min(|P|, |Q|)$ such that $P_j = Q_j$ for all $1 \le j \lt i$ and $P_i \lt Q_i$.
### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains a single integer $N$. The second line contains a binary string $S$ of length $N$.
### Output Format

For each test case, output on a new line the lexicographically minimum string $S$ that can be obtained.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 3\cdot 10^5$
- $S$ is a binary string.
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.
### Sample 1:
Input
Output

```
4
3
110
4
0101
4
0110
6
101011

```

```
110
01
011
01
```

### Explanation:

 **Test case $1$:**  No operations can be performed: only $i = 2$ satisfies $S_i \ne S_{i+1}$, but choosing it splits the string into $11$ and $0$, neither of which contain both zeros and ones.
So, the string cannot be modified, and the answer is $110$ itself.

 **Test case $2$:**  $S = 0101$ initially.
Choose $i = 2$, which is valid because $S_2 \ne S_3$. The string splits into two copies of $01$.
Keep any one copy; the final string is $01$ which is optimal.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-12T15:31:13.577Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here

}

```

---

[View on CodeChef](https://www.codechef.com/problems/BINSPLT)
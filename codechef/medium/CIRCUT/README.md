# CIRCUT

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Monochrome Cut

There is a circle with $N$ points marked on it, numbered $1$ to $N$ in clockwise order.

Point $i$ has value $A_i$ and a color: either red or blue.
The colors are represented by a binary string $S$, where $S_i = 0$ if point $i$ is colored red, and $S_i = 1$ if it's colored blue.

It is guaranteed that there is at least one red point and at least one blue point.

You want to split the points into two groups.
That will be done as follows:

- First, choose two indices $i$ and $j$ ($1 \le i \lt j \le N$) satisfying: $S_i \ne S_{i+1}$, $S_i \ne S_j$, and $S_i = S_{j+1}$
- Then, cut the circle between points $i$ and $i+1$; and also cut the circle between points $j$ and $j+1$.
- This will split the points into two groups: $\{i+1, i+2, \ldots, j\}$ and $\{1, 2, \ldots, i, j+1, \ldots, N\}$.

Note that we're working with cyclic indices, so $S_{N+1} = S_1$.

The condition on the choice of indices $i$ and $j$ really just says that after the groups are formed, the 'endpoints' of one group will both be red, while the 'endpoints' of the other group will both be blue.

The  *score*  of a group of points is the  **maximum value**  that any of them have.

Your task is to find the maximum possible sum of scores of groups, across all valid ways of forming the groups.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input. The first line of each test case contains a single integer $N$. The second line contains $N$ space-separated integers $A_1, \ldots, A_N$. The third line contains the binary string $S$.
### Output Format

For each test case, output on a new line the maximum possible final score.

### Constraints
- $1 \leq T \leq 10^5$
- $2 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \le 10^9$
- $S_i \in \{0, 1\}$
- Both $0$ and $1$ appear in $S$.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.
### Sample 1:
Input
Output

```
4
2
7 3
01
4
4 9 2 6
0110
5
8 3 10 7 5
01011
6
5 9 2 8 6 4
100110

```

```
10
15
18
17
```

### Explanation:

 **Test case $1$:**  There are only two points. So, we must choose $i = 1$ and $j = 2$ for the cut, which separates each point into its own group.
The two groups have scores $7$ and $3$, so the total is $7+3=10$.

 **Test case $2$:**  The only possible valid split is to choose $i = 1$ and $j = 3$, which splits the points into groups $\{1, 4\}$ and $\{2, 3\}$.
The score of the first group is $\max(A_1, A_4) = 6$ while the score of the second group is $\max(A_2, A_3) = 9$, for a total of $15$.

 **Test case $3$:**  Choose $i = 1$ and $j = 5$, which splits the points into $\{1\}$ and $\{2, 3, 4, 5\}$. The groups' scores are $8$ and $10$, for a total of $10+8=18$. This is optimal.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T15:22:37.040Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int x;
    cin >> x;

    while (x--) {
        int n;
        cin >> n;

        vector<long long> a(n);

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        string s;
        cin >> s;

        int z = 0;

        for (int i = 0; i < n; i++) {
            if (s[i] != s[(i + 1) % n]) {
                z++;
            }
        }

        if (z == 2) {
            long long p = 0;
            long long q = 0;

            for (int i = 0; i < n; i++) {
                if (s[i] == '0') {
                    p = max(p, a[i]);
                }
                else {
                    q = max(q, a[i]);
                }
            }

            cout << p + q << '\n';
        }
        else {
            long long p = 0;
            long long q = 0;

            for (int i = 0; i < n; i++) {
                if (a[i] >= p) {
                    q = p;
                    p = a[i];
                }
                else if (a[i] > q) {
                    q = a[i];
                }
            }

            cout << p + q << '\n';
        }
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/CIRCUT)
# MEXMAX7

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Mex and Max

You are given an array $A$ containing $N$ integers. Find the number of non-empty subsequences $B$ of $A$ such that:

- $|\text{mex}(B) - \max(B)| \le 1$

Here, $\text{mex}(B)$ represents the minimum non-negative integer not present in $B$, and $\max(B)$ represents the maximum element of $B$.

Since the answer may be large, find it modulo $998244353$. $2$ subsequences are different if the indices chosen are different, even if the elements are the same.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the number of subsequences satisfying $|\text{mex}(B) - \max(B)| \le 1$ modulo $998244353$.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $0 \le A_i \le N$
### Sample 1:
Input
Output

```
5
3
0 1 2
6
2 2 1 0 0 4
5
0 1 2 3 4
5
1 1 1 2 2
3
3 3 3

```

```
5
34
9
7
0
```

### Explanation:

 **Test Case 1:**  The following are the good subsequences : $[0], [0, 1], [0, 1, 2], [1], [0, 2]$. For example, the first has a $\text{MEX}$ of $1$ and a $\max$ of $0$.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T16:03:58.310Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

#define MOD 998244353

int main() {
    int a;
    cin >> a;

    while (a--) {
        int c;
        cin >> c;

        vector<int> e(c + 2, 0);

        for (int g = 0; g < c; g++) {
            int i;
            cin >> i;
            e[i]++;
        }

        vector<long long> k(c + 2, 0);

        for (int g = 0; g <= c + 1; g++) {
            k[g] = 1;

            for (int i = 0; i < e[g]; i++)
                k[g] = k[g] * 2 % MOD;

            k[g] = (k[g] - 1 + MOD) % MOD;
        }

        long long m = k[1];
        long long n = 1;

        for (int g = 1; g <= c; g++) {
            if (e[g - 1] == 0)
                break;

            n = n * k[g - 1] % MOD;

            // mex = g, max = g - 1
            m = (m + n) % MOD;

            // mex = g, max = g + 1
            if (g + 1 <= c)
                m = (m + n * k[g + 1]) % MOD;
        }

        cout << m << '\n';
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/MEXMAX7)
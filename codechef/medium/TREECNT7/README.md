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
**Submitted:** 2026-08-19T16:15:36.492Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

#define MOD 998244353

long long power(long long a, long long b) {
    long long c = 1;

    while (b > 0) {
        if (b & 1)
            c = c * a % MOD;

        a = a * a % MOD;
        b >>= 1;
    }

    return c;
}

int main() {
    int a;
    cin >> a;

    while (a--) {
        int c;
        cin >> c;

        vector<int> e(c);

        for (int g = 0; g < c; g++)
            cin >> e[g];

        int i = 0;
        int k = 0;

        for (int g = 0; g < c; g++) {
            if (e[g] == 0)
                i++;
            else if (e[g] == 1)
                k++;
        }

        vector<int> m;

        for (int g = 0; g < c; g++) {
            if (e[g] >= 2)
                m.push_back(e[g] - 1);
        }

        int n = m.size();

        vector<vector<long long>> p(i + 1,
                                    vector<long long>(n + 1, 0));

        p[0][0] = 1;

        for (int g = 0; g < n; g++) {
            int q = m[g];

            for (int r = i; r >= q; r--) {
                for (int s = g + 1; s >= 1; s--) {
                    p[r][s] += p[r - q][s - 1];
                    p[r][s] %= MOD;
                }
            }
        }

        vector<long long> t(c + 1, 1);

        for (int g = 0; g <= c; g++)
            t[g] = power(2, g);

        long long u = 0;

        for (int g = 0; g <= i; g++) {
            long long v = 1;

            for (int r = 0; r < g; r++)
                v = v * (i - r) % MOD;

            v = 1;

            // C(i,g)
            long long w = 1;

            for (int r = 1; r <= g; r++) {
                w = w * (i - r + 1) % MOD;
                w = w * power(r, MOD - 2) % MOD;
            }

            for (int r = 0; r <= n; r++) {
                if (p[g][r] == 0)
                    continue;

                for (int s = 0; s <= k; s++) {
                    int x = g + r + s;

                    if (x == 0 || x == c)
                        continue;

                    long long y = 1;

                    // C(k,s)
                    y = 1;

                    for (int z = 1; z <= s; z++) {
                        y = y * (k - z + 1) % MOD;
                        y = y * power(z, MOD - 2) % MOD;
                    }

                    long long z = power(x, c - x - 1);
                    long long h = power(c - x, x - 1);

                    u = (u + p[g][r] * w % MOD *
                             y % MOD * z % MOD * h) % MOD;
                }
            }
        }

        u = u * power(2, MOD - 2) % MOD;

        cout << u << '\n';
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/TREECNT7)
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
**Submitted:** 2026-08-19T16:31:15.986Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

#define MOD 998244353

long long power(long long a, long long b) {
    long long c = 1;

    while (b) {
        if (b & 1)
            c = c * a % MOD;

        a = a * a % MOD;
        b >>= 1;
    }

    return c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a;
    cin >> a;

    while (a--) {
        int c;
        cin >> c;

        vector<int> e(c);

        int g = 0;
        int i = 0;

        for (int k = 0; k < c; k++) {
            cin >> e[k];

            if (e[k] == 0)
                g++;
            else if (e[k] == 1)
                i++;
        }

        vector<int> k;

        for (int x : e) {
            if (x >= 2)
                k.push_back(x - 1);
        }

        int m = g;

        vector<vector<long long>> n(
            k.size() + 1,
            vector<long long>(m + 1, 0)
        );

        n[0][0] = 1;

        int p = 0;

        for (int x : k) {
            p++;

            for (int q = p; q >= 1; q--) {
                for (int r = m; r >= x; r--) {
                    n[q][r] += n[q - 1][r - x];
                    if (n[q][r] >= MOD)
                        n[q][r] -= MOD;
                }
            }
        }

        vector<long long> q(c + 1, 0);

        vector<long long> r(c + 1, 1);
        vector<long long> s(c + 1, 1);

        for (int x = 1; x < c; x++) {
            r[x] = power(x, c - x - 1);
            s[x] = power(c - x, x - 1);
        }

        vector<long long> t(c + 1, 0);

        t[0] = 1;

        for (int x = 1; x <= i; x++) {
            t[x] = t[x - 1] * (i - x + 1) % MOD;
            t[x] = t[x] * power(x, MOD - 2) % MOD;
        }

        vector<long long> u(g + 1, 1);

        for (int x = 1; x <= g; x++) {
            u[x] = u[x - 1] * (g - x + 1) % MOD;
            u[x] = u[x] * power(x, MOD - 2) % MOD;
        }

        vector<long long> v(c + 1, 0);

        for (int x = 1; x < c; x++) {
            long long w = r[x] * s[x] % MOD;
            v[x] = w;
        }

        long long w = 0;

        for (int x = 0; x <= (int)k.size(); x++) {
            for (int y = 0; y <= g; y++) {
                if (n[x][y] == 0)
                    continue;

                if (y > g)
                    continue;

                long long z = u[y];

                for (int h = 0; h <= i; h++) {
                    int j = x + y + h;

                    if (j <= 0 || j >= c)
                        continue;

                    long long aa = t[h];
                    long long bb = n[x][y];

                    long long cc = v[j];

                    long long dd = bb * z % MOD;
                    dd = dd * aa % MOD;
                    dd = dd * cc % MOD;

                    w += dd;

                    if (w >= MOD)
                        w -= MOD;
                }
            }
        }

        w = w * power(2, MOD - 2) % MOD;

        cout << w << '\n';
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/TREECNT7)
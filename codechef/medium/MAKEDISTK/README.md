# MAKEDISTK

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Make Distinct

You're given an array $A$ of length $N$, as well as an integer $K$.

You can perform the following operation on it:

- Choose at most $K$ distinct indices between $1$ and $N$.
- Increment the value at each chosen index by $1$.

Find the minimum number of operations of this type that you need to perform, to obtain an array $A$ where all the elements are pairwise distinct - i.e. $A_i \ne A_j$ must hold for $i \ne j$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains two space-separated integers $N$ and $K$. The second line contains $N$ space-separated integers $A_1, \ldots, A_N$.
### Output Format

For each test case, output on a new line the minimum number of operations needed to obtain an array with pairwise distinct elements.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \le K \le N$
- $1 \le A_i \le 2N$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.
### Sample 1:
Input
Output

```
4
2 1
2 1
4 2
1 1 1 1
6 3
1 3 2 3 2 3
7 4
1 5 2 2 5 5 1

```

```
0
3
3
2

```

### Explanation:

 **Test case $1$:**  $A = [2, 1]$ already contains pairwise distinct elements, so no operations are needed.

 **Test case $2$:**  $A = [1, 1, 1, 1]$ initially, and we can increment at most $K = 2$ elements at once.
One sequence of $3$ operations is as follows:

- Increment the second and third elements. The array is now $[1, 2, 2, 1]$.
- Increment the second and fourth elements. The array is now $[1, 3, 2, 2]$.
- Increment the second and fourth elements again. The array is now $[1, 4, 2, 3]$. All the elements are now pairwise distinct.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-12T15:43:55.471Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;

    while(q--) {
        int z, u;
        cin >> z >> u;

        vector<long long> v(z);

        for(long long &x : v)
            cin >> x;

        sort(v.begin(), v.end());

        auto check = [&](long long r) {
            long long p = v[0];
            long long c = 0;

            for(int i = 1; i < z; i++) {
                long long y = max(v[i], p + 1);

                if(y > v[i] + r)
                    return false;

                c += y - v[i];

                if(c > r * 1LL * u)
                    return false;

                p = y;
            }

            return true;
        };

        long long l = 0;
        long long h = 1LL * z * z;

        while(l < h) {
            long long m = (l + h) / 2;

            if(check(m))
                h = m;
            else
                l = m + 1;
        }

        cout << l << '\n';
    }

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/MAKEDISTK)
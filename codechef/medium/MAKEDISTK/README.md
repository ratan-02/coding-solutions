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
**Submitted:** 2026-08-12T15:42:56.031Z  

```c_cpp
 #include <bits/stdc++.h>
  using namespace std;

  int main() {
      ios::sync_with_stdio(false);
      cin.tie(nullptr);

      int test_cases;
      cin >> test_cases;

      while (test_cases--) {
          int length, limit;
          cin >> length >> limit;

          vector<long long> values(length);

          for (long long &item : values)
              cin >> item;

          sort(values.begin(), values.end());

          auto possible = [&](long long turns) {
              long long previous = values[0];
              long long required = 0;

              if (previous - values[0] > turns)
                  return false;

              for (int pos = 1; pos < length; pos++) {
                  long long chosen = max(values[pos], previous + 1);

                  if (chosen > values[pos] + turns)
                      return false;

                  required += chosen - values[pos];

                  if (required > turns * 1LL * limit)
                      return false;

                  previous = chosen;
              }

              return required <= turns * 1LL * limit;
          };

          long long low = 0;
          long long high = 1LL * length * length;

          while (low < high) {
              long long middle = (low + high) / 2;

              if (possible(middle))
                  high = middle;
              else
                  low = middle + 1;
          }

          cout << low << '\n';
      }

      return 0;
  }
```

---

[View on CodeChef](https://www.codechef.com/problems/MAKEDISTK)
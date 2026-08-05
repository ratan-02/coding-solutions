# Project Euler #1: Multiples of 3 and 5

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

This problem is a programming version of Problem 1 from projecteuler.net

If we list all the natural numbers below that are multiples of or, we get and. The sum of these multiples is.

Find the sum of all the multiples of or below.

 **Input Format** 

First line contains that denotes the number of test cases. This is followed by lines, each containing an integer,.

 **Constraints** 

-
-

 **Output Format** 

For each test case, print an integer that denotes the sum of all the multiples of or below.

 **Sample Input 0** 

```
2
10
100

```

 **Sample Output 0** 

```
23
2318

```

 **Explanation 0** 

For, if we list all the natural numbers below that are multiples of or, we get and. The sum of these multiples is.

Similarly for, we get.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T23:01:55.614Z  

```cpp
#include <iostream>
using namespace std;

long long sumMultiples(long long n, long long k) {
    long long m = (n - 1) / k;
    return k * m * (m + 1) / 2;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long n;
        cin >> n;

        cout << sumMultiples(n, 3)
                + sumMultiples(n, 5)
                - sumMultiples(n, 15)
             << endl;
    }

    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/euler001/problem)
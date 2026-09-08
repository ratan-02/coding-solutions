# GCD of Two

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two positive integers  **a**  and  **b**, find  **GCD** of a and b.

 **Note:**  Don't use the inbuilt gcd function

 **Examples:** 

```
Input: a = 20, b = 28
Output: 4
Explanation: GCD of 20 and 28 is 4
```

```
Input: a = 60, b = 36
Output: 12
Explanation: GCD of 60 and 36 is 12
```

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T07:33:07.114Z  

```cpp
class Solution {
  public:
    int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
};
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1)
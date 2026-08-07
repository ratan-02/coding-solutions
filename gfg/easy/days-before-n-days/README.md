# Day Before n Days

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two integers  **d**  and  **n.** Where  **d**  is the day, out of 7 days of the week,  **d**  varies from 0 to 6 as shown below.
0 - Sunday
1 - Monday
2 - Tuesday
3 - Wednesday
4 - Thursday
5 - Friday
6 - Saturday

You need to return the index for the day which is  **n**  days before the given day  **d.** 

 **Examples:** 

```
Input: d = 4, n = 3
Output: 1
Explanation: 3 days before the 4th is 1.
```

```
Input: d = 2, n = 19
Output: 4
Explanation: 19 days before the 2nd is 4.

```

 **Constraints:** 
0 ≤ d ≤ 6
0 ≤ n ≤ 109

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-07T15:52:24.941Z  

```cpp
class Solution {
  public:
    int nthDay(int d, int n) {
        return (d - (n % 7) + 7) % 7;
    }
};
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/days-before-n-days/1)
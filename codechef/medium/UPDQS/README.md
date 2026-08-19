# UPDQS

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Update Queries

For an array $A$, define $f(A)$ as the  **minimum sum**  of the array $A$ possible by using the following operation multiple times (possibly $0$):

- Choose an index $i$ ($1 < i < N$) and update $A_i = A_{i + 1} + A_{i - 1} - A_i$.

You are given an array $A$ of $N$ integers.

There are $Q$ updates:

- Given integers $i$ and $x$, update $A_i = x$ permanently.
- Find $f(A)$ after each update.
### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains $2$ integers - $N$ and $Q$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$. The next $Q$ lines contain $2$ integers each - $i$ and $x$, representing a query.
### Output Format

For each test case, output $Q$ integers, the answers after each update.

### Constraints
- $1 \le T \le 10^4$
- $2 \le N \le 2 \cdot 10^5$
- $1 \le Q \le 2 \cdot 10^5$
- $1 \le A_i \le 10^7$
- $1 \le i \le N$
- $1 \le x \le 10^7$
- The sum of $N$ and the sum of $Q$ both do not exceed $2 \cdot 10^5$
### Sample 1:
Input
Output

```
2
3 3
1 2 3
2 6
3 10
1 12
5 2
10 3 7 1 15
4 6
4 1

```

```
2
16
28
36
26
```

### Explanation:

 **Test Case 1:**  The following are the answers after each update:

- After update $1$: The array is $[1, 6, 3]$. We can perform an operation with $i = 2$ to get $[1, -2, 3]$ which has a sum of $2$.
- After update $2$ : The array is $[1, 6, 10]$. We can perform an operation with $i = 2$ to get $[1, 5, 10]$ which has a sum of $16$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T16:31:57.982Z  

```py
from collections import deque

def find_min_sum(arr):
    n = len(arr)
    if n <= 2:
        return sum(arr)
    
    seen = set()
    queue = deque()
    
    initial_tuple = tuple(arr)
    queue.append(initial_tuple)
    seen.add(initial_tuple)
    
    min_sum = sum(arr)
    
    while queue:
        current = queue.popleft()
        current_sum = sum(current)
        min_sum = min(min_sum, current_sum)
        
        current_list = list(current)
        
        for i in range(1, n - 1):
            new_arr = current_list[:]
            new_arr[i] = current_list[i + 1] + current_list[i - 1] - current_list[i]
            new_tuple = tuple(new_arr)
            
            if new_tuple not in seen:
                seen.add(new_tuple)
                new_sum = sum(new_arr)
                if new_sum < min_sum:
                    queue.append(new_tuple)
                    min_sum = new_sum
    
    return min_sum

def solve():
    t = int(input())
    
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(map(int, input().split()))
        
        for _ in range(q):
            i, x = map(int, input().split())
            arr[i - 1] = x
            
            result = find_min_sum(arr)
            print(result)

if __name__ == "__main__":
    solve()
```

---

[View on CodeChef](https://www.codechef.com/problems/UPDQS)
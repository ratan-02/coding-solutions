# THREEGAME

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Three Player Game

You are organizing a simple $3$-player game. It consists of several rounds, each round being won by exactly one of the $3$ players.

You have decided to conduct at least $N$ rounds, but if after $N$ rounds there is no clear winner; you will conduct additional rounds till there is a clear winner. A clear winner is one who has won strictly more games than the other $2$ players.

Find the maximum number of rounds you may have to conduct.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of input contains a single integer $N$.
### Output Format

For each test case, output on a new line the maximum number of rounds you may have to conduct.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^9$
### Sample 1:
Input
Output

```
3
1
2
3

```

```
1
4
4
```

### Explanation:

 **Test Case 1:**  After $1$ game, there is always a clear winner (the person who won that game).

 **Test Case 2:**  Here is a possible way the game could last $4$ rounds:

- Person $1$ wins round $1$.
- Person $2$ wins round $2$. $2$ games are up, but persons $1$ and $2$ are tied.
- Person $3$ wins round $3$. Everybody is tied.
- Person $3$ wins round $4$, and is the clear winner.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-02T15:57:38.111Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    while(T--) {
        long long N;
        cin >> N;
        
        long long remainder = N % 3;
        long long answer;
        
        if (remainder == 0) {
            answer = N + 1;
        } else if (remainder == 1) {
            answer = N;
        } else {  // remainder == 2
            answer = N + 2;
        }
        
        cout << answer << endl;
    }
    
    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/THREEGAME)
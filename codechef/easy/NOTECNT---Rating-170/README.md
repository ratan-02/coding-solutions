# NOTECNT - Rating 170

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Notebook Counting

Chef has $A$ notebooks with him, each having a total of $B$ pages.

Each page has $50$ lines drawn to be written on, and you can write on both sides of the pages. Chef has to follow the drawn lines when writing. Thus, he can only write $50$ lines on the front side of the page, and $50$ lines on the back side.

What is the effective total number of lines that Chef can write across all his notebooks?

### Input Format
- The first and only line of input contains $2$ integers - $A$ and $B$.
### Output Format

For each test case, output on a new line the total number of lines Chef can write.

### Constraints
- $1 \le A \le 10$
- $1 \le B \le 100$
### Sample 1:
Input
Output

```
1 1

```

```
100

```

### Explanation:

Chef has $1$ notebook with $1$ page only. He can write $50$ lines on the front, and $50$ lines on the back side of the page, for a total of $100$ lines.

### Sample 2:
Input
Output

```
5 50

```

```
25000

```

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T22:49:59.985Z  

```c_cpp
#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    cout << A * B * 100 << endl;

    return 0;
}
```

---

[View on CodeChef](https://www.codechef.com/problems/NOTECNT)
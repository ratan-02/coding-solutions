# SSNK - Rating 196

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Snaky Strings

Chef calls a string  *snaky*  if it either starts or ends with the letter `'s'`.

You are given a string $A$ of length $4$, consisting of only lowercase English letters.
Is the string $A$  *snaky* ?

### Input Format
- The only line of input contains a string $A$ of length $4$, containing only lowercase English letters.
### Output Format

Output a string denoting the answer: `Yes` if the string $A$ is  *snaky*  and `No` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. the strings `NO`, `No`, `nO`, and `no` will be treated as equivalent.

### Constraints
- $A$ has length $4$.
- Every character of $A$ is a lowercase English letter, i.e. one of $\{\tt{a}, \tt{b}, \ldots, \tt{z}\}$.
### Sample 1:
Input
Output

```
hiss

```

```
Yes
```

### Explanation:

The string `"hiss"` ends with the letter `'s'`, so it is  *snaky*.

### Sample 2:
Input
Output

```
rock

```

```
No
```

### Explanation:

The string `"rock"` neither starts nor ends with the letter `'s'`, so it is not  *snaky*.

### Sample 3:
Input
Output

```
snow

```

```
Yes
```

### Explanation:

The string `"snow"` starts with the letter `'s'`, so it is  *snaky*.

## Solution

**Language:** c_cpp  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-19T03:29:33.031Z  

```c_cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
	string s;
	cin >> s;
	if(s[0] =='s' || s[3] == 's' ){
	    cout << "YES" ;
	}
	else{
	    cout << "NO" ;
	}
	return 0;
	
	
}

```

---

[View on CodeChef](https://www.codechef.com/problems/SSNK)
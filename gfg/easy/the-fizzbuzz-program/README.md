# The FizzBuzz Program

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a number  **n,**  print your answer according to the following conditions:

- If the number is divisible by 3, you print Fizz
- If the number is divisible by 5, you print Buzz
- If the number is divisible by both 3 and 5, you print FizzBuzz
- In any other case, you print the number itself

 **Examples:** 

```
Input: n = 3
Output: Fizz
Explanation: Here, the number is divisible by 3, so Fizz is printed.
```

```
Input: n = 5
Output: Buzz
Explanation: Here the number is divisible by 5, so Buzz is printed.
```

```
Input: number = 15
Output: FizzBuzz
Explanation: Here, the number 15 is divisible by both 3 and 5, so FizzBuzz is printed.

```

```
Input: number = 7
Output: 7
Explanation: 7 is not divisible by 3 or 5.
```

 **Constraints:** 

1 <= n <= 100

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T23:06:30.734Z  

```cpp
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string fizzBuzz(int n) {
        if (n % 3 == 0 && n % 5 == 0)
            return "FizzBuzz";
        else if (n % 3 == 0)
            return "Fizz";
        else if (n % 5 == 0)
            return "Buzz";
        else
            return to_string(n);
    }
};

int main() {
    int n;
    cin >> n;

    Solution obj;
    cout << obj.fizzBuzz(n);

    return 0;
}
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-fizzbuzz-program/1)
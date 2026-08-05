# Length of Last Word

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` consisting of words and spaces, return  *the length of the  **last**  word in the string.* 

A  **word**  is a maximal substring consisting of non-space characters only.

 

 **Example 1:** 

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

```

 **Example 2:** 

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

```

 **Example 3:** 

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

```

 

 **Constraints:** 

- 1 <= s.length <= 104
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.

## Solution

**Language:** C++  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 9 MB (beats 34.83%)  
**Submitted:** 2026-08-05T22:41:57.386Z  

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;
        
        while (i >= 0 && s[i] == ' ') {
            i--;
        }
        
        int len = 0;
       
        while (i >= 0 && s[i] != ' ') {
            len++;
            i--;
        }
        
        return len;
    }
};
```

---

[View on LeetCode](https://leetcode.com/problems/length-of-last-word/)
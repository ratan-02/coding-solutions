# Find the K-th Character in String Game I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a  **positive**  integer `k`.

Now Bob will ask Alice to perform the following operation  **forever** :

- Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `kth` character in `word`, after enough operations have been done for `word` to have  **at least**  `k` characters.

 

 **Example 1:** 

 **Input:**  k = 5

 **Output:**  "b"

 **Explanation:** 

Initially, `word = "a"`. We need to do the operation three times:

- Generated string is "b", word becomes "ab".
- Generated string is "bc", word becomes "abbc".
- Generated string is "bccd", word becomes "abbcbccd".

 **Example 2:** 

 **Input:**  k = 10

 **Output:**  "c"

 

 **Constraints:** 

- 1 <= k <= 500

## Solution

**Language:** C++  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 7.8 MB (beats 81.95%)  
**Submitted:** 2026-09-07T03:31:49.096Z  

```cpp
class Solution {
public:
    char kthCharacter(int k) {
        int shifts = 0;

        while (k > 1) {
            int len = 1;
            while (len * 2 < k)
                len *= 2;

            if (k > len) {
                k -= len;
                shifts++;
            }
        }

        return 'a' + shifts;
    }
};
```

---

[View on LeetCode](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/)
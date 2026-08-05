# Strings

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

C++ provides a nice alternative data type to manipulate strings, and the data type is conveniently called _string_. Some of its widely used features are the following:

- *Declaration:*
	
    	string a = "abc";
        
- *Size:* 

		int len = a.size();

- *Concatenate two strings:*

		string a = "abc";
        string b = "def";
        string c = a + b; // c = "abcdef".

- *Accessing $i^{th}$ element:*

        string s = "abc";
        char   c0 = s[0];	// c0 = 'a'
        char   c1 = s[1];	// c1 = 'b'
        char   c2 = s[2];	// c2 = 'c'
        
        s[0] = 'z';			// s = "zbc"



*P.S.:* We will use _cin/cout_ to read/write a string.

**Input Format**

You are given two strings, $a$ and $b$, separated by a new line. Each string will consist of lower case Latin characters ('a'-'z').

**Constraints**

 

**Output Format**

In the first line print two space-separated integers, representing the length of $a$ and $b$ respectively.  
In the second line print the string produced by concatenating $a$ and $b$ ($a+b$).  
In the third line print two strings separated by a space, $a'$ and $b'$. $a'$ and $b'$ are the same as $a$ and $b$, respectively, except that their first characters are swapped.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-05T22:59:43.233Z  

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    // Lengths
    cout << a.size() << " " << b.size() << endl;

    // Concatenation
    cout << a + b << endl;

    // Swap first characters
    char temp = a[0];
    a[0] = b[0];
    b[0] = temp;

    cout << a << " " << b << endl;

    return 0;
}

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/c-tutorial-strings/problem)
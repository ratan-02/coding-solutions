# Implement Trie (Prefix Tree)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A  **trie**  (pronounced as "try") or  **prefix tree**  is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

 

 **Example 1:** 

```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

```

 

 **Constraints:** 

- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 104 calls in total will be made to insert, search, and startsWith.

## Solution

**Language:** C++  
**Runtime:** 31 ms (beats 71.48%)  
**Memory:** 50.6 MB (beats 31.04%)  
**Submitted:** 2026-11-26T07:06:43.201Z  

```cpp
class Trie {
public:
    struct Node {
        Node* links[26];
        bool flag;

        Node() {
            for(int i = 0; i < 26; i++)
                links[i] = NULL;
            flag = false;
        }
    };

    Node* root;

    Trie() {
        root = new Node();
    }

    void insert(string word) {
        Node* node = root;

        for(char ch : word) {
            int idx = ch - 'a';

            if(node->links[idx] == NULL)
                node->links[idx] = new Node();

            node = node->links[idx];
        }

        node->flag = true;
    }

    bool search(string word) {
        Node* node = root;

        for(char ch : word) {
            int idx = ch - 'a';

            if(node->links[idx] == NULL)
                return false;

            node = node->links[idx];
        }

        return node->flag;
    }

    bool startsWith(string prefix) {
        Node* node = root;

        for(char ch : prefix) {
            int idx = ch - 'a';

            if(node->links[idx] == NULL)
                return false;

            node = node->links[idx];
        }

        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

---

[View on LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/)
# 🔠 Longest Common Prefix — LeetCode Solution

LeetCode Problem: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

---

## 🧩 Problem Summary

Write a function to find the **longest common prefix string** among an array of strings.

If there is no common prefix, return an empty string `""`.

---

## 🧠 Approach

The solution uses a **horizontal scanning** approach:
1. Start by assuming the first word is the longest possible prefix.
2. Compare it against each remaining word in the list.
3. Shrink the prefix character by character (`prefix = prefix[:-1]`) until all strings start with it.

---

## ✅ Python Solution

```python
class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
```

---

## 🧪 Example

```python
Input: ["flower", "flow", "flight"]
Output: "fl"
```

---

## 📝 Explanation

- Start with prefix = `"flower"`
- Compare with `"flow"` → reduce to `"flow"` → `"flo"` → `"fl"`
- Compare `"fl"` with `"flight"` → valid
- ✅ Result: `"fl"`

---

## 💡 Notes

- Efficient for small arrays or strings with early mismatches.
- Time complexity: `O(S)` where `S` is the sum of all characters in all strings.
- Space complexity: `O(1)`

---

## 🏷️ Tags

`String` `Prefix Matching`

---

## 📜 License

This solution is provided by the user and is free to use for educational purposes.

# LeetCode Problem 9: Palindrome Number

**Link:** [Palindrome Number – LeetCode](https://leetcode.com/problems/palindrome-number/)

## Problem Summary:
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

- An integer is a palindrome when it reads the same backward as forward.
- Negative numbers are **not** palindromes.

### Example:
```
Input: x = 121
Output: true

Input: x = -121
Output: false

Input: x = 10
Output: false
```

---

## Approach:

- Convert the integer to a string.
- Compare the string with its reverse using slicing (`[::-1]`).
- Return `True` if they are equal, `False` otherwise.

This approach is straightforward and leverages Python's string manipulation capabilities.

---

## Python Code:
```python
class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]: 
            return True
        else: 
            return False
```

---

## Complexity:
- **Time Complexity:** O(n), where n is the number of digits in `x`
- **Space Complexity:** O(n), due to the string conversion

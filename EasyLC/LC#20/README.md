
# 🧩 Valid Parentheses — LeetCode Solution

LeetCode Problem: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## 🧩 Problem Summary

Given a string `s` containing just the characters `()[]{}`, determine if the input string is **valid**.

A string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

---

## 🧠 Approach

This solution uses a **stack** to keep track of open brackets:

1. When encountering an opening bracket, push it onto the stack.
2. When encountering a closing bracket:
   - Check if the stack is not empty.
   - Check if the top of the stack matches the corresponding opening bracket.
   - If not, return `False`.
3. At the end, the stack should be empty if the string is valid.

---

## ✅ Python Solution

```python
class Solution(object):
    def isValid(self, s):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in pair.values():  # opening brackets
                stack.append(char)
            elif char in pair:  # closing brackets
                if not stack or stack[-1] != pair[char]:
                    return False
                stack.pop()

        return not stack
```

---

## 🧪 Example

```python
Input: s = "()[]{}"
Output: True

Input: s = "(]"
Output: False
```

---

## 💡 Notes

- This solution runs in **O(n)** time and uses **O(n)** space in the worst case.
- Handles nested and mixed bracket types correctly.

---

## 🏷️ Tags

`Stack` `String` `Validation`

---

## 📜 License

Solution provided by the user, free to reuse and learn from.

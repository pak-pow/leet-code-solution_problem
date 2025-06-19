
# 🏛️ Roman to Integer — LeetCode Solution

LeetCode Problem: [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)  
Submission: [#1669032008](https://leetcode.com/problems/roman-to-integer/submissions/1669032008/)

---

## 🧩 Problem Summary

Convert a Roman numeral string (e.g., `"IX"`, `"LVIII"`) into its corresponding integer value.

Roman numerals are based on the following symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Special subtractive rules:
- `IV` = 4  
- `IX` = 9  
- `XL` = 40  
- `XC` = 90  
- `CD` = 400  
- `CM` = 900  

---

## 🧠 Approach

The solution uses a **greedy left-to-right traversal** to process Roman characters. It checks for subtractive pairs and adjusts accordingly.

---

## ✅ Python Solution

```python
class Solution(object):
    def romanToInt(self, s):

        values = {      
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }       

        self.i = 0
        self.total = 0       

        while self.i < len(s):

            if (self.i + 1 < len(s) and values[s[self.i]] < values[s[self.i + 1]]):
                self.total += values[s[self.i + 1]] - values[s[self.i]]
                self.i += 2
            else:
                self.total += values[s[self.i]]
                self.i += 1

        return self.total
```

---

## 📝 Example

```python
Input: "MCMXCIV"
Output: 1994

# Breakdown:
# M (1000) + CM (900) + XC (90) + IV (4) = 1994
```

---

## 💡 Notes

- This solution handles both additive and subtractive Roman numeral rules.
- It maintains readability while efficiently processing the input in a single pass.
- Uses class-level variables `self.i` and `self.total` for clarity and flow control.

---

## 🏷️ Tags

`Greedy` `String` `Hash Map`

---

## 📜 License

Solution authored by [pak-pow](https://leetcode.com/pak-pow/), free to reuse for study or educational purposes.

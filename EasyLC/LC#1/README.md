# LeetCode Problem 1: Two Sum

**Link:** [Two Sum – LeetCode](https://leetcode.com/problems/two-sum/)

## Problem Summary:
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

- Each input has **exactly one solution**.
- You may not use the same element twice.
- You can return the answer in any order.

### Example:
```
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9
```

---

## Approach:

- Use a **hash map (`dict`)** to store previously seen numbers and their indices.
- For each number in the array, check if its complement (i.e., `target - num`) exists in the hash map.
- If it exists, return the current index and the stored index of the complement.
- This approach ensures **O(n)** time complexity.

---

## Python Code (Solution I Made):
```python
class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []
```



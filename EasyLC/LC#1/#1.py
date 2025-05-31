class Solution:

    def two_sum(self, num_list, set_target):

        lookup = {}  # to store number: index

        for i, num in enumerate(num_list):

            complement = set_target - num

            if complement in lookup:
                return [lookup[complement], i]

            lookup[num] = i

        return None  # return None if no valid pair is found

# Get input from user
num_list = []
user_input = input("Enter an array: ").strip("[]").split(",")

for num in user_input:
    if num.strip():  # skip empty strings from something like "[2,,3]"
        num_list.append(int(num.strip()))

set_target = int(input("Set target: "))

solution = Solution()
result = solution.two_sum(num_list, set_target)

print("Result:", result)

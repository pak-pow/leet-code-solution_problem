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


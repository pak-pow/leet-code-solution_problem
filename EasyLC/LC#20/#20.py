class Solution(object):
    def isValid(self, s):
        
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}

        for char in s:
            
            if char in pair.values():
                stack.append(char)
            
            elif char in pair:  
                
                if not stack or stack[-1] != pair[char]:
                    return False
                    
                stack.pop()
        
        return not stack

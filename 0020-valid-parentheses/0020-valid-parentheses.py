class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '}' or c == ']' or c == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(' and c != ')':
                    return False
                elif stack[-1] == '{' and c != '}':
                    return False
                elif stack[-1] == '[' and c != ']':
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False
                
                
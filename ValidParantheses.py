class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    return False
                elif stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0:
                    return False
                elif stack.pop() != '{':
                    return False
            elif c == ']':
                if len(stack) == 0:
                    return False
                elif stack.pop() != '[':
                    return False

        if len(stack) > 0:
            return False
        return True


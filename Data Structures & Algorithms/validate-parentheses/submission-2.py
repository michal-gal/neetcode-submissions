class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'{':'}', '(':')', '[':']'}
        for letter in s:
            if letter in mapping:
                stack.append(letter)
                continue
            if not stack:
                return False
            elif letter == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
        
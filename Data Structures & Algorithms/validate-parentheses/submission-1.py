class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter in '({[':
                stack.append(letter)
                continue
            if stack == []:
                return False
            elif letter ==']' and stack[-1] == '[':
                stack.pop()
            elif letter ==')' and stack[-1] == '(':
                stack.pop()
            elif letter =='}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return stack == []
        
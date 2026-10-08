class Solution:

    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for x in operations:
            #print(f'{stack}, {x}')
            if x == 'C':
                stack.pop()
                #print(stack)
            elif x == '+':
                stack.append(stack[-1]+stack[-2])
                #print(stack)
            elif x == 'D':
                stack.append(2*stack[-1])
                #print(stack)
            else:
                stack.append(int(x))

        return sum(stack)
            

        
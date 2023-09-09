class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for j in tokens:
            if j not in ('+','-','*','/'):
                stack.append(j)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if j=='/':
                    stack.append(num1/num2)
                elif j=='*':
                    stack.append(num1*num2)
                elif j=='+':
                    stack.append(num1+num2)
                else:
                    stack.append(num1-num2)
        return int(stack[-1])

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for j in range(len(temperatures)):
            if len(stack)==0:
                stack.append(j)
            else:
                while len(stack)>0 and temperatures[j]>temperatures[stack[-1]]:
                    #print(stack,temperatures[j],stack[-1])
                    popped = stack.pop()
                    result[popped] = j-popped
                stack.append(j)
        
        return result
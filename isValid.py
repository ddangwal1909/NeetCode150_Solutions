class Solution:
    
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {'}':'{', ']':'[',')':'('}
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif i in ['{','(','[']:
                stack.append(i)
            else:
                ele = stack.pop()
                if ele!=mapping[i]:
                    return False
        
        if len(stack)>0:
            return False
        
        return True
        
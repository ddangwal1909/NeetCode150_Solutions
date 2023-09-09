class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = set()

        def next_bracket(open,close,current):
            if open<0 or close<0:
                return 
            if open==0 and close==0:
                #print(current)
                result.add(current)
                return
            else:
                ### 
                next_bracket(open-1,close,current+'(')
                if open<close:
                    next_bracket(open,close-1,current+')')
        
        next_bracket(n,n,'')
        return list(result)
                
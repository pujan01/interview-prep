class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(c, o, n):
            if c == n:
                res.append("".join(stack)) 
                return
            
            if o < n:
                stack.append("(")
                backtrack(c, o + 1, n)
                stack.pop()
                
            if c < o:
                stack.append(")")
                backtrack(c+1, o, n)
                stack.pop()

        backtrack(0,0,n)
        return res 



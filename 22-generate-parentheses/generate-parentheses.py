class Solution:
    def generateParenthesis(self, n: int) -> List[str]:




        stack = [] # this will hold all parenthesis temporarily
        result = [] #final list




        #definding recursive function to backtrace and fill all combinations of parenthesis

        def backtrace(openN, closeN):

            if openN == closeN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrace(openN+1,closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrace(openN,closeN+1)
                stack.pop()

        backtrace(0,0)
        return result
















        '''res = []

        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open

        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs("")
        return res'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo={}
        def helper(m,n,op):
                if op == "+":
                    return m+n
                elif op == "-":
                    return m-n
                else:
                    return m*n
        
        def dfs(expression):
            
            
            ##smallest valid input, digit
            if expression.isdigit():
                return [int(expression)]
            if expression in memo:
                return memo[expression]
            
            res=[]
            for i in range(len(expression)):
                if expression[i] in "+-*":
                    ##split
                    resleft=dfs(expression[:i])
                    resright=dfs(expression[i+1:])
                    
                    ##Return left and right list
                    
                    for j in resleft:
                        for k in resright:
                            res.append(helper(j,k,expression[i]))
            memo[expression]=res
            return res
        
        return dfs(expression)
           

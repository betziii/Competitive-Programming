class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = 1
        num = 0
        stack = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)     
            elif c in "-+":
                res += sign * num
                num = 0                    
                sign = 1 if c == '+' else -1
            elif c == '(':                  
                stack.append(res)          
                stack.append(sign)          
                sign, res = 1, 0            
            elif c == ')':
                res += sign * num
                res *= stack.pop()          
                res += stack.pop()          
                num = 0                     

        return res + num * sign

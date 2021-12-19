class Solution:
    def isValid(self, s: str) -> bool:
#         stack = []
#         balanced = False
#         n = len(s)
#         for i in s:
#             if i=='(' or i == '[' or i =='{':
#                 stack.append(i)
#                 print (stack)
#             else:   
#                 balanced = False
#                 break
#         for i in s:
#             if len(stack) !=0:
#                 print(stack)
#                 if i == ')' or i ==']' or i == '}':
#                     m = stack.pop()
#                     print(m)
#                     if m == '(' and i==')':
#                         balanced = True
#                     elif m == '[' and i==']':
#                         balanced = True
#                     elif m == '{' and i=='}':
#                         balanced = True
#                     else:
#                         balanced = False
#                         break
#             else:
#                 balanced = False
#                 break

            
#         # print (stack)
#         return balanced
        # def isValidParentheses(parentheses):
        p = {"{":"}", "[":"]", "(":")"}
        stack = []
        for i in range(len(s)):
            if s[i] in p.keys():
                stack.append(s[i])
            else:
                if (len(stack) == 0):
                        return False
                if (s[i] == p[stack[-1]]):
                    stack.pop()
                else:
                    return False
        if (len(stack) == 0):
            return True
        else:
            return False
                    
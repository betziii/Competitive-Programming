class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        result = 0
        for i in tokens:
            if i.isdigit() == True or i.lstrip('-').replace('.', '', 1).isdigit():
                s.append(i)
            elif i == '+' and len(s) >=2:
                m = int(s.pop())
                result = m + int(s.pop())
                s.append(result)
                # print(s)
            elif i == '-' and len(s) >=2:
                m = int(s.pop())
                result = int(s.pop()) -m
                s.append(result)
                # print(s)
            elif i == '*' and len(s) >=2:
                m = int(s.pop())
                result = m * int(s.pop())
                s.append(result)
                # print(s)
            elif i == '/' and len(s) >=2:
                m = int(s.pop())
                result = int(s.pop()) / m
                s.append(int(result))
                # print(s)
            else:
                return 0
        return s.pop()
                
                
                
                
                
                
                
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        
        while a or b:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                #if ans[-1] == 'b': wa = True else: False
                wa = ans[-1] == 'b'
            else:
                wa = a >= b

            if wa:
                a -= 1
                ans.append('a')
            else:
                b -= 1
                ans.append('b')

        return "".join(ans)
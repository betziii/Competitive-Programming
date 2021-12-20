class Solution:
    def reverseParentheses(self, s: str) -> str:
        stacks=[]
        for i in s:

            if i!=')':
                stacks.append(i)
                # print(st)

            else:
                r=''
                while(stacks!=[] and stacks[-1]!='('):
                      r+=stacks.pop()
                      # print(r)
                stacks.pop()
                stacks.append(r[::-1])
                # print(stacks)



        for i in range(len(stacks)):
            stacks[i]=stacks[i][::-1]
            # print (stacks[i])


        return "".join(stacks)        
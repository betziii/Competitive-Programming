ca=s.count('a')
        cb=0
        result=float('inf')
        for ch in s:
            if(ch=='a'): 
                ca-=1
                result=min(result,ca+cb)
            elif(ch=='b'): 
                cb+=1
                result=min(result,ca+cb-1)
        return result

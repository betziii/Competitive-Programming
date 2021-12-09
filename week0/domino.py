m,n = map(int, input().split())

def Domino(m,n):
    res = 0
    if (m % 2 ==0):
        res = (m//2) * n
    else:
        res = ((m//2) * n) + n//2
    print(res)
    
Domino(m,n)
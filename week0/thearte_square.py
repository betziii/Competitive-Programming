#n,m,a = map(int, input().split())
n = eval(input("n"))
m = eval(input("m"))
a = eval(input("a"))
def Square(n,m,a):
    countn = 0
    countm = 0
    result= 0
    
    if n % a !=0:
        countn = (n//a) + 1
    else:
        countn = (n//a)
    if m % a !=0:
        countm = (m//a) + 1
    else:
        countm = (m//a)
    result = countm * countn
    return result
    
print(Square(6,6,4))

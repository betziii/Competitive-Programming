n = int(input())
t = input().split(' ')

one = 0
two = 0

n=input()
t=map(int,input().split())
ls=[]
l=t[0]
count=1
for i in t[1:]:
    if i==l:
        count+=1
    else:
        l=i
        ls.append(count)
        c=1
    ls.append(count)
m=0
for i in range(1,len(ls)):
    m=max(m,2*min(ls[i],ls[i-1]))
print (m)



for i in range(n):
    if t[i] == '1' and t[i+1] == '2':
        one += 1
    elif t[i] == '2' and t[i+1] == '1':
        two += 1
if one <= two:
    print(one * 2)
else: 
    print(two * 2)


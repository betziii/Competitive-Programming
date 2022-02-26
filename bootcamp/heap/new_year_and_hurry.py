n,k = input().split(" ")
n,k = int(n),int(k)

def new():
    n,k = input().split(" ")
    n,k = int(n),int(k)
    sums = 0
    t = 240 - k
    count = 0
    for i in range(1, n+1):
        sums += 5 * i
        if sums > t:
            break
        count +=1
    print(count)
        
new()
# ls = []
# t = 240 - k
# for i in range(1, n+1):
#     if len(ls)> 0:
#         ls.append((5 * i) + ls[len(ls)-1])
#     else: 
#         ls.append(5 * i)
# if len(ls) == 1:
#     if ls[0] <= t:
#         print(1)
#     else:
#         print(0)
# else:
#     l = 0
#     r = len(ls)-1
#     while l < r:
#         mid = l + (r-l)//2
#         if ls[mid] <= t:
#             print(ls.index(mid)+1)
#         # elif ls[mid] < t:
#         #     l = mid + 1
#         elif ls[mid] > t:
#             r = mid + 1 
            
    
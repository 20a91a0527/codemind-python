a=int(input())
l=0
while a>0:
    r=a%10
    if l<r:
        l=r
    a=a//10
print(l)
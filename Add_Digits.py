a=int(input())
s=0
while a>0 or s>9:
    if a==0:
        a=s
        s=0
    r=a%10
    s+=r
    a=a//10
print(s)
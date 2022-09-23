a=int(input())
c=d=0
while a>0:
    r=a%10
    if r%2==0:
        c+=1
    else:
        d+=1
    a=a//10
if c>0 and d>0:
    print("Mixed")
elif c==0 and d>0:
    print("Odd")
else:
    print("Even")
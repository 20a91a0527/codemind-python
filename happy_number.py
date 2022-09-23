a=int(input())
s=0
while a>0 or s>9:
    if a==0:
        a=s
        s=0
    r=a%10
    s+=r*r
    a=a//10
if s==1 or s==7:
    print("True")
else:
    print("False")
    
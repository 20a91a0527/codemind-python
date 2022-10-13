x=int(input())
s=x*x
c=0
while s>0:
    r=s%10
    c+=r
    s=s//10
if c==x:
    print("Neon Number")
else:
    print("Not Neon Number")
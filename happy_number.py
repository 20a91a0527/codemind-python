n=int(input())
s=0
while 1:
    while n>0:
        r=n%10
        s+=r*r
        n=n//10
    if s<10 and s==1:
        print('True')
        break
    elif s<10 and s!=1:
        print('False')
        break
    else:
        n=s
        s=0
x=int(input())
f=0
s=1
t=f+s
if x==0:
    print(0)
while t<=x:
    f=s
    s=t
    t=f+s
if(abs(t-x)>abs(s-x)):
    print(s)
elif abs(t-x)==abs(s-x):
    print(s,t)
else:
    print(t)
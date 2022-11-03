n=input()
l=[]
for i in n:
    l.append(i)
k=set(l)
x=list(k)
if len(x)==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")
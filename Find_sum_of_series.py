n=int(input())
c=0
d=0
for i in range(1,n+1):
    c=1/(1+(i-1))
    d+=c
print("{:.2f}".format(d))

x,y=map(int,input().split())
if ((x*1)+(y*2))%2!=0:
    print("NO")
elif x==0 and y%2!=0:
    print("NO")
elif y==0 and x%2!=0:
    print("NO")
else:
    print("YES")
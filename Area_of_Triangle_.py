a,b,c=map(int,input().split())
import math
s=(a+b+c)/2
x=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("{:.2f}".format(x))
a=int(input())
b=int(input())
s=0
x=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range (1,b):
    if b%j==0:
        x+=j
if s==b and x==a:
    print("Amicable")
else:
    print("Not Amicable")
        
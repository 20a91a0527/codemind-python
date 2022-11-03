n=int(input())
a=n*n
if n<10:
    r=a%10
elif n>=10 and n<99:
    r=a%100
elif n>=100 and n<999:
    r=a%1000
elif n>=1000 and n<9999:
    r=a%10000
if n==r:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
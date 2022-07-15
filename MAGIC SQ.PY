a=[[2,7,6],
   [9,5,1],
   [4,3,8]]
i=0
r1=0
r2=0
r3=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            r1+=a[i][j]
        elif i==1:
            r2+=a[i][j]
        else:
            r3+=a[i][j]
        j+=1
    i+=1
if r1==r2==r3:
    print(r1,r2,r3)
i=0
c1=0
c2=0
c3=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if j==0:
            c1+=a[i][j]
        elif j==1:
            c2+=a[i][j]
        else:
            c3+=a[i][j]
        j+=1
    i+=1
if c1==c2==c3:
    print(c1,c2,c3)
i=0
d1=0
d2=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==j:
            d1+=a[i][j]
        if i+j==2:
            d2+=a[i][j]
        j+=1
    i+=1
if d1==d2:
    print(d1,d2)
if r1==r2==r3==c1==c2==c3==d1==d2:
    print("it is magic square")
else:
    print("it is not magic square")
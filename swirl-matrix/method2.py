nr=int(input("Enter the number of rows :"))
nc=int(input("Enter the number of columns :"))

n=nr*nc

r=[]
for i in range(nr):
    r.append(i)
c=[]
for i in range(nc):
    c.append(i)

path=[]
while n!=0:


    lr=len(r)
    lc=len(c)
    for i in c:
        x=str(i)
        y=str(r[0])
        position=y+x
        path.append(position)
        n-=1
    r.pop(0)
    #print(path)

    if n==0:
        break
    
    lr=len(r)
    lc=len(c)
    for i in r:
        x=str(c[lc-1])
        y=str(i)  
        position=y+x
        path.append(position)
        n-=1
    c.pop(lc-1)
    #print(path)

    if n==0:
        break

    lr=len(r)
    lc=len(c)
    c.reverse()
    for i in c:
        x=str(i)
        y=str(r[lr-1])
        position=y+x
        path.append(position)
        n-=1
    c.reverse()
    r.pop(lr-1)
    #print(path)

    if n==0:
        break

    lr=len(r)
    lc=len(c)
    r.reverse()
    for i in r:
        x=str(c[0])
        y=str(i)
        position=y+x
        path.append(position)
        n-=1
    r.reverse()
    c.pop(0)
    #print(path)

print(path)

m= [[0 for i in range(nc)] for j in range(nr)] 
print(m)

n=nr*nc

#to take only integers in as an array input
#elements=list(map(int,input("enter integer elements in a space separated array :").split()))

elements=[]
for i in range(n):
    elem=input("Enter the elements of the matrix:")
    elements.append(elem)

for i in range(n):
    position=path[i]
    x=int(position[1])
    y=int(position[0])
    m[y][x]=elements[i]
print(m)

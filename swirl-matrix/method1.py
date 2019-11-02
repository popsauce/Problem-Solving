n=int(input("number of elements"))
l=[]
rows=int(input("num of rows"))
columns=int(input("num of columns"))

for i in range(n):
    m=int(input("enter all elements"))
    l.append(m)
print(l)


m= [[0 for i in range(columns)] for j in range(rows)] 
print(m)


length=len(l)


x=0
y=0
a=1
while length!=0:
    
    while y<columns:
        m[x][y]=l[0]
        if a==1 or (a-1)/4==0:
            y=y+1
        else:
            y=y-1
        l.pop(0)
        length-=1
        #print(m)
        """
        print(x, end="")
        print(y)
        print("##")
        """
    if a==1 or (a-1)/4==0:
        x=x+1
        y=y-1
    else:
        x=x-1
        y=y+1
    columns-=1
    a+=1
    """
    print(x, end="")
    print(y)
    print("##")
    """
    while x<rows:
        m[x][y]=l[0]
        if a==2 or (a-2)/4==0:
            x=x+1
        else:
            x=x-1
        l.pop(0)
        length-=1
        #print(m)
        """
        print(x, end="")
        print(y)
        print("##")
        """
    if a==2 or (a-2)/4==0:
        y=y-1
        x=x-1
    else:
        x=x+1
        y=y+1
    rows-=1
    a+=1
    """
    print(x, end="")
    print(y)
    print("##")
    """
print(m)

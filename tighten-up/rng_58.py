def point_in_triangle(xa,xb,xc,ya,yb,yc,px,py):
    val=0
    
    ax=xa
    bx=xb
    cx=xc
    ay=ya
    by=yb
    cy=yc
    if point_on_same_side(ax,bx,cx,ay,by,cy,px,py)==1:
        val+=1
    
    ax=xa
    bx=xc
    cx=xb
    ay=ya
    by=yc
    cy=yb
    if point_on_same_side(ax,bx,cx,ay,by,cy,px,py)==1:
        val+=1
    
    ax=xc
    bx=xb
    cx=xa
    ay=yc
    by=yb
    cy=ya
    if point_on_same_side(ax,bx,cx,ay,by,cy,px,py)==1:
        val+=1
    
    if val==3:
        return(1)
    else:
        return(0)

def point_on_same_side(ax,bx,cx,ay,by,cy,px,py):
    #print("exec")
    if bx-ax!=0:
        m=(by-ay)/(bx-ax)
        sp=1
    else:
        m=by-ay
        sp=0
    
    pt_in_eqn=sp*(py-ay)-m*(px-ax)
    tript_in_eqn=sp*(cy-ay)-m*(cx-ax)
    if tript_in_eqn==0:
        return(0)

    elif tript_in_eqn>0 and pt_in_eqn>=0:
        #print("yesp")
        return(1)
        
    elif tript_in_eqn<0 and pt_in_eqn<=0:
        #print("yesn")
        return(1)
        
    else:
        #print("none?")
        return(0)

def pins_replace_vertice(pins_in_triangle,xa,xb,xc,ya,yb,yc):



"""
triangle_pts=list(map(int,input().split()))

xa=triangle_pts[0]
xb=triangle_pts[1]
xc=triangle_pts[2]
ya=triangle_pts[3]
yb=triangle_pts[4]
yc=triangle_pts[5]
px=triangle_pts[6]
py=triangle_pts[7]

ans=point_in_triangle(xa,xb,xc,ya,yb,yc,px,py)
print(ans)

"""
stop=0
while stop!=1:
    ini=list(map(int,input().split()))
    m=ini[0]
    n=ini[1]
    vertlist=[]
    pinlist=[]
    for vertice in range(m):
        pt=list(map(int,input().split()))
        vertlist.append(pt)
    for pins in range(n):
        pt=list(map(int,input().split()))
        pinlist.append(pt)


    free_thr=1
    while free_thr!=0:
        rem=[]
        for i in range(len(vertlist)-2):
            xa=vertlist[i][0]
            ya=vertlist[i][1]
            xb=vertlist[i+1][0]
            yb=vertlist[i+1][1]
            xc=vertlist[i+2][0]
            yc=vertlist[i+2][1]
            cont=1
            for j in range(len(pinlist)):
                px=pinlist[j][0]
                py=pinlist[j][1]
                if point_in_triangle(xa,xb,xc,ya,yb,yc,px,py)==1:
                    cont=0
                    break
            if cont==1:
                rem.append(vertlist[i+1])
        free_thr=0
        if len(rem)!=0:
            free_thr=1
            for i in rem:
                vertlist.remove(i)
    
    for i in range(len(vertlist)-2):
        xa=vertlist[i][0]
        ya=vertlist[i][1]
        xb=vertlist[i+1][0]
        yb=vertlist[i+1][1]
        xc=vertlist[i+2][0]
        yc=vertlist[i+2][1]
        pins_in_triangle=[]
        for j in pinlist:
            px=j[0]
            py=j[1]
            if point_in_triangle(xa,xb,xc,ya,yb,yc,px,py)==1:
                pins_in_triangle.append(j)
        insrt=pins_replace_vertice(pins_in_triangle,xa,xb,xc,ya,yb,yc)
        vertlist.pop(i+1)
        pins_at_ends.append(insrt[0])
        l=len(insrt)
        pins_at_ends.append(insrt[l])
        vertlist[i+1:i+1]=insrt
        
        
    print(vertlist)
    stop=1


"""
    remove_st_lines=[]
    for i in range(len(vertlist)-2):
        xa=vertlist[i][0]
        ya=vertlist[i][1]
        xb=vertlist[i+1][0]
        yb=vertlist[i+1][1]
        xc=vertlist[i+2][0]
        yc=vertlist[i+2][1]
        if math.sqrt(((xc-xa)**2)+((yc-ya)**2))==math.sqrt(((xc-xb)**2)+((yc-yb)**2))+math.sqrt(((xb-xa)**2)+((yb-ya)**2))
            remove_st_lines.append(vertlist[i+1])
    for i in remove_st_lines:
        vertlist.remove(i)
"""

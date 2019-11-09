
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
    if bx-ax!=0:
        m=(by-ay)/(bx-ax)
        sp=1
    else:
        m=by-ay
        sp=0
    
    pt_in_eqn=sp*(py-ay)-m*(px-ax)
    tript_in_eqn=sp*(cy-ay)-m*(cy-ax)
    if tript_in_eqn>0 and pt_in_eqn>0:
        return(1)
        
    elif tript_in_eqn<0 and pt_in_eqn<0:
        return(1)
        
    else:
        return(0)
        

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
""" 

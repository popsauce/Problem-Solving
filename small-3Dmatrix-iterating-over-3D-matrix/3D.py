bw=int(input("Enter the width of big matrix"))
br=int(input("Enter num of rows of big matrix"))
bc=int(input("Enter num of cols of big matrix"))
sw=int(input("Enter the width of small matrix"))
sr=int(input("Enter num of rows of small matrix"))
sc=int(input("Enter num of cols of small matrix"))

bigthreedee=[]
for i in range(bw):
    ma=[]
    for j in range(br):
        val=list(map(int,input("Enter the elements of a row in a big matrix").split()))
        ma.append(val)
    print("Big Matrix :- ")
    print(ma)
    bigthreedee.append(ma)
print("big 3d :- ")
print(bigthreedee)

smallthreedee=[]
for i in range(sw):
    mi=[]
    for i in range(sr):
        val=list(map(int,input("Enter the elements of a row in a small matrix").split()))
        mi.append(val)
    print("Small Matrix :- ")
    print(mi)
    smallthreedee.append(mi)
print("small 3d:-")
print(smallthreedee)

# bigthreedee=[[[4,3,4],[3,2,3],[4,3,4]],[[3,2,3],[2,1,2],[3,2,3]],[[4,3,4],[3,2,3],[4,3,4]]]
# smallthreedee=[[[1,1],[1,1]],[[1,1],[1,1]]]

print("Iterations :- ")
#mlist=[]
for i in range(bw-sw+1):
    for j in range(br-sr+1):
        for k in range(bc-sc+1):
            threedee=[]
            for p in range(sw):    
                cm=[]
                #multiplier=0
                for q in range(sr):
                    cr=[]
                    for r in range(sc):
                        #multiplier+=bigthreedee[i+p][j+q][k+r]*smallthreedee[p][q][r]
                        val=bigthreedee[i+p][j+q][k+r]
                        cr.append(val)
                    cm.append(cr)
                threedee.append(cm)
            #mlist.append(multiplier)
            print(threedee)
#print(mlist)

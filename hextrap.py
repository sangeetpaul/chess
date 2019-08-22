def mk(n):
    B[c][c]=1
    i=c; j=c; e=1
    for d in range(1,n): # tier
        j+=1; e+=1 # initial east
        B[i][j]=e
        for k in range(d-1): # south-east
            i+=1; j+=1; e+=1
            B[i][j]=e
        for k in range(d): # south
            i+=1; e+=1
            B[i][j]=e
        for k in range(d): # west
            j-=1; e+=1
            B[i][j]=e
        for k in range(d): # north-west
            i-=1; j-=1; e+=1
            B[i][j]=e
        for k in range(d): # north
            i-=1; e+=1
            B[i][j]=e
        for k in range(d): # east
            j+=1; e+=1
            B[i][j]=e

def sm(i,j):
    mini=i; minj=j; mine=wall
    knight=[[-1,2],[-2,1],[-3,-1],[-3,-2],[-2,-3],[-1,-3],[1,-2],[2,-1],[3,1],[3,2],[2,3],[1,3]]
    for xy in knight:
        x=i+xy[0]; y=j+xy[1]
        if x>=0 and x<m and y>=0 and y<m and B[x][y]<mine:
            mini=x; minj=y; mine=B[x][y]
    return [mini,minj,mine]
f = open('b327132.txt', 'w')
for n in range(1,201): # n>=4
    c=n-1; m=2*n-1; wall=3*n**2-3*n+2
    B=[[wall]*m for i in range(m)]
    mk(n)
    
    mov=[]; i=c; j=c; cell=1
    while(cell<wall):
        mov.append(cell)
        B[i][j]=wall
        mins=sm(i,j)
        i,j,cell=mins
    f.write(str(n)+' '+str(mov[-1])+'\n')
f.close()
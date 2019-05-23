def path(m):
    def mkB(): # spiral Board numbering
        B[c][c]=1
        i=c; j=c; e=1
        for d in range(1,m,2): # tier
            for k in range(d): # right
                j+=1; e+=1
                B[i][j]=e
            for k in range(d): # down
                i+=1; e+=1
                B[i][j]=e
            for k in range(d+1): # left
                j-=1; e+=1
                B[i][j]=e
            for k in range(d+1): # up
                i-=1; e+=1
                B[i][j]=e
        for k in range(m-1): # last right
            j+=1; e+=1
            B[i][j]=e
    def smK(i,j): # smallest move for Knight/Horse
        mini=i; minj=j; mine=M
        if i-1>=0 and j+2<m and B[i-1][j+2]<mine:
            mini=i-1; minj=j+2; mine=B[i-1][j+2]
        if i-2>=0 and j+1<m and B[i-2][j+1]<mine:
            mini=i-2; minj=j+1; mine=B[i-2][j+1]
        if i-2>=0 and j-1>=0 and B[i-2][j-1]<mine:
            mini=i-2; minj=j-1; mine=B[i-2][j-1]
        if i-1>=0 and j-2>=0 and B[i-1][j-2]<mine:
            mini=i-1; minj=j-2; mine=B[i-1][j-2]
        if i+1<m and j-2>=0 and B[i+1][j-2]<mine:
            mini=i+1; minj=j-2; mine=B[i+1][j-2]
        if i+2<m and j-1>=0 and B[i+2][j-1]<mine:
            mini=i+2; minj=j-1; mine=B[i+2][j-1]
        if i+2<m and j+1<m and B[i+2][j+1]<mine:
            mini=i+2; minj=j+1; mine=B[i+2][j+1]
        if i+1<m and j+2<m and B[i+1][j+2]<mine:
            mini=i+1; minj=j+2; mine=B[i+1][j+2]
        return [mini,minj,mine]
    def smF(i,j): # smallest move for Ferz
        mini=i; minj=j; mine=M
        if i-1>=0 and j+1<m and B[i-1][j+1]<mine:
            mini=i-1; minj=j+1; mine=B[i-1][j+1]
        if i-1>=0 and j-1>=0 and B[i-1][j-1]<mine:
            mini=i-1; minj=j-1; mine=B[i-1][j-1]
        if i+1<m and j-1>=0 and B[i+1][j-1]<mine:
            mini=i+1; minj=j-1; mine=B[i+1][j-1]
        if i+1<m and j+1<m and B[i+1][j+1]<mine:
            mini=i+1; minj=j+1; mine=B[i+1][j+1]
        return [mini,minj,mine]
    c=int(m/2); M=m*m+1
    B=[[0]*m for i in range(m)] # mxm board
    mkB()
    mov=[]; i=c; j=c; k=1
    while(k<M):
        mov.append(k)
        B[i][j]=M
        mins=smF(i,j)
        i,j,k=mins
    return(mov)

trap=[]
for t in range(1,100,2):
    trap.append(path(t)[-1])
print(trap)

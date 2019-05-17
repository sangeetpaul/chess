def mkB(): # make Board
    c=int(m/2) # center
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

m=5 # m is Odd
B=[[0]*m for i in range(m)]
mkB()

import datetime as dt
beg=dt.datetime.now()
import numpy as np
'''
def safe(i,j): # check for rooks in way
    if np.sum(A, axis=0)[j]>0 or np.trace(A, offset=j-i)>0:
        return False
    return True
'''
def rot(A): # rotate 60 deg cc
    R=np.zeros((d,d), dtype=int)
    for i in range(d):
        for j in range(max(0,i-a+1),min(d,i+a)):
            R[i][j]=A[j][j-i+a-1]
    return R
def ref(A): # reflect
    R=np.transpose(A)
    return R
def uniq(S,A): # is A unique wrt S?
    X=np.empty((0,d,d), dtype=int) # set of A variants
    B=rot(A); C=rot(B); D=rot(C); E=rot(D); F=rot(E)
    if (B==A).all(): # hexad
        pass
    elif (C==A).all(): # triad
        X=np.append(X,[B], axis=0)
    elif (D==A).all(): # dyad
        X=np.append(X,[B,C], axis=0)
    else: # no rot sym
        X=np.append(X,[B,C,D,E,F], axis=0)
    M=ref(A); m=0
    for x in X:
        if (M==x).all(): # ref sym
            m=1; break
    if m==0: # no ref sym
        if (B==A).all():
            X=np.append(X,[M], axis=0)
        elif (C==A).all():
            X=np.append(X,[M,ref(B)], axis=0)
        elif (D==A).all():
            X=np.append(X,[M,ref(B),ref(C)], axis=0)
        else:
            X=np.append(X,[M,ref(B),ref(C),ref(D),ref(E),ref(F)], axis=0)
    for x in X:
        for s in S:
            if (x==s).all():
                return False
    return True
'''
def show(A):
    print('\n'),
    for i in range(d):
        for j in range(abs(i-a+1)):
            print(''),
        for j in range(max(0,i-a+1),min(d,i+a)):
            print(A[i][j]),
        print('\n'),
'''
a=8 # edge length
d=2*a-1 # diameter
'''
A=np.zeros((d,d), dtype=int) # board
R=[0]*d # rook tracker
S=np.empty((0,d,d), dtype=int) # set of unique solutions
i,j=0,3; c=0
while i>0 or j<4:#a/2:
    if i<d: # empty rows
        if j<d and j<i+a: # not end of row
            if safe(i,j)==True:
                A[i][j]=1 # place rook
                R[i]=j # record location
                i+=1 # next row
                j=0 if i<a else i-a+1 # start of row
            else:
                j+=1 # next in row
        else: # end of row
            i-=1 # previous row
            A[i][R[i]]=0 # remove rook
            j=R[i]+1 # next in row
    else: # all rows filled
        if uniq(S,A)==True:
            S=np.append(S, [A], axis=0); c+=1
            if c%2000==0:
                np.save('3/'+str(c/2000),S)
                S=np.empty((0,d,d), dtype=int)
        i-=1 # previous (last) row
        A[i][R[i]]=0 # remove rook
        j=R[i]+1 # next in (last) row
np.save('3/'+str(int(c/2000)+1),S)
print('Unique solutions =',c)
'''
nxt=2
in1='1-'+str(nxt-1)
in2='1/'+str(nxt)
out='1-'+str(nxt)
I1=np.load(in1+'.npy'); I2=np.load(in2+'.npy')
O=I1
for i2 in I2:
    if uniq(I1,i2)==True:
        O=np.append(O, [i2], axis=0)
np.save(out,O)

end=dt.datetime.now()
print('Time =',end-beg)
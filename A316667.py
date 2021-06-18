import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import board
import piece

radius = 30
max_label = (2*radius+1)**2
B = board.Spiral(radius)
N = piece.Knight((radius,radius),'white')
B.array[radius,radius] = N
B.label[radius,radius] = max_label
min_label = 0
rows = [radius]
cols = [radius]
labels = [0]
while True:
    rs, cs, _ = N.get_vision(B)
    argmin = np.argmin(B.label[rs, cs])
    min_label = B.label[rs[argmin],cs[argmin]]
    if min_label<max_label:
        rows.append(rs[argmin])
        cols.append(cs[argmin])        
        labels.append(min_label)
        B.move(N.location, (rs[argmin],cs[argmin]))
        B.label[rs[argmin],cs[argmin]] = max_label
    else:
        break
rows = np.array(rows)
cols = np.array(cols)
labels = np.array(labels)

points = np.array([cols, rows]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
fig,ax = plt.subplots(1,1,figsize=(10,10))
norm = plt.Normalize(0, len(labels)-1)
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(np.arange(0,len(labels)))
line = ax.add_collection(lc)
ax.plot(cols[0],rows[0],'r.')
ax.plot(cols[-1],rows[-1],'r.')
ax.set_xlim(0, 2*radius)
ax.set_ylim(0, 2*radius)
ax.invert_yaxis()
fig.tight_layout()
fig.savefig('./plots/A316667.png')
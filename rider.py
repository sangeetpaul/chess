import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from tqdm import tqdm
import board
import piece

MN = [(2,1),(3,1),(3,2),(4,1),(4,3),(5,1),(5,2),(5,3),(5,4),(6,1),(6,5),
      (7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(8,1),(8,3),(8,5),(8,7),
      (9,1),(9,2),(9,4),(9,5),(9,7),(9,8),(10,1),(10,3),(10,7),(10,9)]

for m,n in tqdm(MN):
    min_radius = 10
    max_radius = 100
    radius = min_radius
    dr = 10
    
    while radius<=max_radius:
        max_label = (2*radius+1)**2
        B = board.Spiral(radius)
        N = piece.Rider((radius,radius),[(m,n)],'white')
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
                old_location = N.location
                B.move(old_location, (rs[argmin],cs[argmin]))
                r,c = old_location
                B.array[r,c] = piece.Pawn(old_location,'white')
                B.label[rs[argmin],cs[argmin]] = max_label
            else:
                break
        rows = np.array(rows)
        cols = np.array(cols)
        labels = np.array(labels)
        
        bcs = np.logical_or.reduce([rows.min()<m,
                                    rows.max()>2*radius-m,
                                    cols.min()<m,
                                    cols.max()>2*radius-m])
        if bcs:
            radius += dr
        else:
            if dr>1:
                radius -= dr
                dr //= 10
                radius += dr
            else:
                break
    
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
    ax.axhline(m,c='k',alpha=0.5)
    ax.axhline(2*radius-m,c='k',alpha=0.5)
    ax.axvline(m,c='k',alpha=0.5)
    ax.axvline(2*radius-m,c='k',alpha=0.5)
    ax.invert_yaxis()
    ax.set_title(f'({m},{n})-rider: radius={radius}, step={len(labels)-1}, square={labels[-1]}')
    fig.tight_layout()
    fig.savefig(f'./plots/riders/rider_{m}_{n}.png')
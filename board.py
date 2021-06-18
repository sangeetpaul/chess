import numpy as np
import piece

class Board:
    def __init__(self,array=None,n_dimensions=None):
        if isinstance(array,np.ndarray):
            self.array = array
            self.n_dimensions = array.shape
        elif isinstance(array,str):
            self.array = str2nda(array)
            self.n_dimensions = self.array.shape
        else:
            self.n_dimensions = n_dimensions
            self.array = np.array([[None]*n_dimensions[1]]*n_dimensions[0])
    def __repr__(self):
        rep = '.\n'
        for r in range(self.n_dimensions[0]):
            for c in range(self.n_dimensions[1]):
                if self.array[r,c] == None:
                    rep += '-'
                else:
                    rep += notation[type(self.array[r,c])]
            rep += '\n'
        rep += '.'
        return rep
    def get_piece(self,r,c):
        if 0<=r<self.n_dimensions[0] and 0<=c<self.n_dimensions[1]:
            return self.array[r,c]
        else:
            return 'out'
    def move(self,dep,arr):
        dep_r,dep_c = dep
        arr_r,arr_c = arr
        piece = self.get_piece(dep_r,dep_c)
        self.array[dep_r,dep_c] = None
        self.array[arr_r,arr_c] = piece
        piece.location = (arr_r,arr_c)
    def get_pieces(self):
        pieces = []
        for r in range(self.n_dimensions[0]):
            for c in range(self.n_dimensions[1]):
                if self.array[r,c] != None:
                    pieces.append(self.array[r,c])
        return pieces
    def get_blank(self):
        return np.array([[None]*self.n_dimensions[1]]*self.n_dimensions[0])

class Standard(Board):
    def __init__(self):
        super().__init__(
            '''
            RbNbBbQbKbBbNbRb
            PbPbPbPbPbPbPbPb
            ----------------
            ----------------
            ----------------
            ----------------
            PwPwPwPwPwPwPwPw
            RwNwBwQwKwBwNwRw
            ''',
            None)

class Spiral(Board):
    def __init__(self,radius):
        super().__init__(None,(2*radius+1,2*radius+1))
        self.label = np.empty_like(self.array, int)
        l, r, c = 0, radius, radius
        self.label[r,c] = l
        for rad in range(radius): # right
            c += 1
            l += 1
            self.label[r,c] = l
            for _ in range(2*rad+1): # up
                r -= 1
                l += 1
                self.label[r,c] = l
            for _ in range(2*rad+2): # left
                c -= 1
                l += 1
                self.label[r,c] = l
            for _ in range(2*rad+2): # down
                r += 1
                l += 1
                self.label[r,c] = l
            for _ in range(2*rad+2): # right
                c += 1
                l += 1
                self.label[r,c] = l

def str2nda(string):
    S = string.split()
    n_dimensions = (len(S), len(S[0])//2)
    array = np.array([[None]*n_dimensions[1]]*n_dimensions[0])
    for r in range(n_dimensions[0]):
        for c in range(n_dimensions[1]):
            if S[r][2*c] != '-':
                P = S[r][2*c]
                color = 'white' if S[r][2*c+1]=='w' else 'black'
                array[r,c] = notation_inv[P]((r,c),color)
    return array

notation = {
    piece.Pawn: 'P',
    piece.Rook: 'R',
    piece.Knight:'N',
    piece.Bishop: 'B',
    piece.Queen: 'Q',
    piece.King: 'K'
    }

notation_inv = {v: k for k, v in notation.items()}
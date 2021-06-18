#import numpy as np

class Piece:
    def __init__(self, location, color):
        self.location = location
        self.color = color

class Leaper(Piece):
    def __init__(self, location, strides, color):
        super().__init__(location, color)
        self.strides = strides
    def get_vision(self, board):
        rs,cs,ps = [],[],[]
        loc_r,loc_c = self.location
        for stride in self.strides:
            str_r,str_c = stride
            if str_c==0:
                dir_r = [0,-str_r,0,str_r]
                dir_c = [str_r,0,-str_r,0]
            else:
                dir_r = [-str_c,-str_r,-str_r,-str_c,str_c,str_r,str_r,str_c]
                dir_c = [str_r,str_c,-str_c,-str_r,-str_r,-str_c,str_c,str_r]
            for i in range(len(dir_r)):
                p = board.get_piece(loc_r+dir_r[i],loc_c+dir_c[i])
                if p=='out':
                    pass
                else:
                    rs.append(loc_r+dir_r[i])
                    cs.append(loc_c+dir_c[i])
                    ps.append(p)
        vision = [rs,cs,ps]
        return vision

class Rider(Piece):
    def __init__(self, location, strides, color):
        super().__init__(location, color)
        self.strides = strides
    def get_vision(self, board):
        rs,cs,ps = [],[],[]
        loc_r,loc_c = self.location
        for stride in self.strides:
            str_r,str_c = stride
            if str_c==0:
                dir_r = [0,-str_r,0,str_r]
                dir_c = [str_r,0,-str_r,0]
            else:
                dir_r = [-str_c,-str_r,-str_r,-str_c,str_c,str_r,str_r,str_c]
                dir_c = [str_r,str_c,-str_c,-str_r,-str_r,-str_c,str_c,str_r]
            for i in range(len(dir_r)):
                step = 1
                while True:
                    p = board.get_piece(loc_r+step*dir_r[i],loc_c+step*dir_c[i])
                    if p==None:
                        rs.append(loc_r+step*dir_r[i])
                        cs.append(loc_c+step*dir_c[i])
                        ps.append(p)
                        step += 1
                    elif p=='out':
                        break
                    else:
                        rs.append(loc_r+step*dir_r[i])
                        cs.append(loc_c+step*dir_c[i])
                        ps.append(p)
                        break
        vision = [rs,cs,ps]
        return vision

class Rook(Rider):
    def __init__(self, location, color):
        super().__init__(location, [(1,0)], color)

class Bishop(Rider):
    def __init__(self, location, color):
        super().__init__(location, [(1,1)], color)

class Knight(Leaper):
    def __init__(self, location, color):
        super().__init__(location, [(2,1)], color)

class Queen(Rider):
    def __init__(self, location, color):
        super().__init__(location, [(1,0),(1,1)], color)

class King(Leaper):
    def __init__(self, location, color):
        super().__init__(location, [(1,0),(1,1)], color)

class Pawn(Piece):
    def __init__(self, location, color):
        super().__init__(location, color)
        self.unmoved = True
    def get_vision(self, board):
        rs,cs,ps = [],[],[]
        loc_r,loc_c = self.location
        dir_f = -1 if self.color=='white' else 1
        dir_r = [loc_r+r for r in [dir_f,dir_f]]
        dir_c = [loc_c+c for c in [1,-1]]
        for i in range(len(dir_r)):
            p = board.get_piece(dir_r[i],dir_c[i])
            if p not in [None,'out']:
                rs.append(dir_r[i])
                cs.append(dir_c[i])
                ps.append(p)
        p = board.get_piece(loc_r+dir_f,0)
        if p==None:
            rs.append(loc_r+dir_f)
            cs.append(0)
            ps.append(p)
            if self.unmoved:
                p = board.get_piece(loc_r+2*dir_f,0)
                if p==None:
                    rs.append(loc_r+2*dir_f)
                    cs.append(0)
                    ps.append(p)
        vision = [rs,cs,ps]
        return vision

class Masque:
    
    def __init__(self):
        self.taille = 0
        self.tableau = [[]]
                
    def GetValeur(self,x,y):
        return self.tableau[x][y]
                
    def GetTaille(self):
        return self.taille
        

class Brighten(Masque):

    def __init__(self):
        self.taille = 1
        self.tableau = [[1.5]]
        
class Darken(Masque):

    def __init__(self):
        self.taille = 1
        self.tableau = [[.5]]


class EdgeVertical(Masque):

    def __init__(self,size):
        self.taille = size
        self.tableau = [[0]*size]*size
        
        for y in range(size):
            self.tableau[0][y] = -1
            self.tableau[size-1][y] = 1
                        
class EdgeHorizontal(Masque):

    def __init__(self,size):
        self.taille = size
        self.tableau = [[0]*size]*size
        
        for x in range(size):
            self.tableau[x][0] = 1
            self.tableau[x][size-1] = -1
            
class Blur(Masque):

    def __init__(self,size):
        self.taille = size
        self.tableau = [[1/pow(size, 2)]*size]*size

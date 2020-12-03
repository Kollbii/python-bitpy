import matplotlib.pyplot as plt
import numpy as np
import random
import os
np.set_printoptions(threshold=np.inf)
 
class Board:
    def __init__(self):
        pass

    def createBoard(self,dim):
        self.dim = dim
        self.board = np.zeros((self.dim,self.dim),dtype= "object")    

    def place_on_board_random(self,n):
        self.n = n  #ilosc hetmanuw
        self.cords = []
        
        for _ in range(self.n):
             
            x,y = random.randint(0,self.dim-1), random.randint(0,self.dim-1)
            new_cord = (x,y)
            if new_cord in self.cords:
                while True:
                    x,y = random.randint(0,self.dim-1), random.randint(0,self.dim-1)
                    new_cord = (x,y)
                    if new_cord not in self.cords:
                        self.cords.append(new_cord)
            else:
                self.cords.append(new_cord)


            
        for cord in self.cords:
            self.board[cord[0]][cord[1]] = 'H'

        print("simea")
        return self.board

    def writeToFile(self):
        np.savetxt("board1.txt",self.board, fmt='%s', delimiter=' ')

    

p = os.getcwd()
if os.path.exists(p+"/board.txt") == True:
    os.remove(p+"/board.txt")



b = Board()
b.createBoard(10)
tablica = b.place_on_board_random(10)
print(tablica)
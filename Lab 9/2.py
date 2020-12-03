import matplotlib.pyplot as plt
import numpy as np
import random
import os

class Board:
    def createBoard(self,dim):
        #dim to wymiar, board to początkowo macierz 2-wymiarowa wypełniona zerami
        self.dim = dim
        self.board = np.zeros((self.dim,self.dim),dtype= "object")    

    def place_on_board_random(self,n):
        #n to ilość hetmanów, cords to lista zawierająca krotkę ich koordynatów (x,y)
        self.n = n
        self.cords = []
        
        for _ in range(self.n):
            #tworzenie koordynatów pionków
            x,y = random.randint(0,self.dim-1), random.randint(0,self.dim-1)
            new_cord = (x,y)

            #instrukcje warunkowe generujące całą listę dla podanej liczby koordynatów
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

        return self.board

    def writeToFile(self):
        #zapis do pliku
        np.savetxt("board1.txt",self.board, fmt='%s', delimiter=' ')

    def assignHetmanToCord(self):
        #takie dictionary comprehension, mogło być użyte ale nie zostało
        hetman_name = [(f"hetman{x}",self.cords[x]) for x in range(self.n)]
        self.hetman_dict = {k:v for k,v in hetman_name}
        
        return self.hetman_dict

    def checkTakeDown(self):
        #dwie listy, jedna zawiera elementy nieszachujące, druga wykluczone, te które się szachują
        self.not_checked = []
        self.excluded = []
        for i in range(0,self.n):
            self.takedown = False

            for j in range(i+1,self.n):
                #koordynaty dwóch kolejnych pionków
                x1 = self.cords[i][1]
                y1 = self.cords[i][0]

                x2 = self.cords[j][1]
                y2 = self.cords[j][0]
                
                #instrukcje warunkowe, dwie ostatnie korzystają z liczenia nachylenia - tangens 45,135,225 i 315
                if x1 == x2:
                    self.takedown = True
                    self.excluded.append(self.cords[i])
                    self.excluded.append(self.cords[j])

                elif y1 == y2:
                    self.takedown = True
                    self.excluded.append(self.cords[i])
                    self.excluded.append(self.cords[j])
                
                elif x2 - x1 == y2 - y1:                  #kąt 45 i 225        
                    self.takedown = True
                    self.excluded.append(self.cords[i])
                    self.excluded.append(self.cords[j])

                elif -x2 + x1 == y2 - y1:                 #kąt 135 i 315
                    self.takedown = True
                    self.excluded.append(self.cords[i])
                    self.excluded.append(self.cords[j])
                    
            #warunek dodania do listy zawierającej nieszachujące
            if self.takedown == False and self.cords[i] not in self.excluded and self.cords[j] not in self.excluded:
                self.not_checked.append(self.cords[i])
                self.not_checked.append(self.cords[j])

        #nadmiarowe usuwanie, czasami niektóre koordynaty mogły przejść, a tego nie chcieliśmy
        for wyklucz in self.excluded:
            if wyklucz in self.not_checked:
                self.not_checked.remove(wyklucz)
        
        if len(self.not_checked) == 0:
            print("wszystkie hetmany sie szachuja")
            return self.not_checked

        else:
            print("nie wszystkie hetmany sie szachuja")
            return self.not_checked        

    
    def tryToPlot(self):
        for kord in self.not_checked:
            self.board[kord] = 0.5
        
        #plotowanie na plansze, 1 to szachujące, 0.5 to nieszachujące
        plot_arr = self.board
        plot_arr = np.where(plot_arr == 'H', 1, plot_arr)
        plot_arr = plot_arr.astype(np.float32)
        plt.matshow(plot_arr)
        plt.colorbar()
        plt.show()

#usuwanie pliku
p = os.getcwd()
if os.path.exists(p+"/board.txt") == True:
    os.remove(p+"/board.txt")

dim = int(input("podaj wymiar planszy: "))
n = int(input("podaj ilość pionków: "))

#inicjalizacja obiektu i wykonywanie metod na rzecz tego obiektu
b = Board()
b.createBoard(dim)
b.place_on_board_random(n)
b.writeToFile()
b.checkTakeDown()
b.tryToPlot()
print(b.assignHetmanToCord()) #nieuzywane ale mozna pokazac 
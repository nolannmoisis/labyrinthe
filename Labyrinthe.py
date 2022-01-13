# -*- coding: utf-8 -*-
import csv

class Labyrinthe:
    
    def get_entreeX(self):
        return self._entreeX
    
    def get_entreeY(self):
        return self._entreeY
    
    def get_entreeX(self):
        return self._sortieX
    
    def get_entreeX(self):
        return self._sortieY
        
    def __init__(self):
        self._carteLaby=[]
        csvfile=open("Laby.csv")
        lecteur = csv.reader(csvfile,delimiter=',')
        for ligne in lecteur:
            self._carteLaby.append(ligne)
    
        self._entreeX = 0
        self._entreeY = 8
        self._sortieX = 9
        self._sortieY = 1
        
    def dessin(self):
        fill(0,0,0)
        stroke(10,10,255)
        strokeWeight(1)
        
        for i in range (len(self._carteLaby)):
            for j in range (len(self._carteLaby[0])):
                if self._carteLaby[i][j]=='1':
                    rect(j*40,i*40,40,40)
                
        
        
    

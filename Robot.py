# -*- coding: utf-8 -*-
class robot:
        
    def get_posX(self):
        return self._entreeX
    
    def get_posY(self):
        return self._entreeY
    
    def get_direc(self):
        return self._direc
    
    def __init__(self,posX,posY,direc):
        self._posX=posX
        self._posY=posY
        self._direc=direc
        
    def dessin(self):
        fill(200,200,200)
        stroke(0,0,0)
        strokeWeight(0)
        X=self._posX*40+20
        Y=self._posY*40+20
        ellipse(X,Y,35,35)
        
        XN=self._posX*40+20
        YN=self._posY*40+5
        XS=self._posX*40+20
        YS=self._posY*40+35
        XO=self._posX*40+5
        YO=self._posY*40+20
        XE=self._posX*40+35
        YE=self._posY*40+20
        
        fill(0,255,255)
        
        if self._direc == "NORD":
            triangle(XN,YN,XO,YO,XE,YE)
        
        if self._direc == "SUD":
            triangle(XS,YS,XO,YO,XE,YE)
            
        if self._direc == "EST":
            triangle(XN,YN,XS,YS,XE,YE)
            
        if self._direc == "OUEST":
            triangle(XN,YN,XO,YO,XS,YS)
            
    def bouge(self):
        if key == "d":
            self._direc="EST"
        if key == "s":
            self._direc="SUD"
        if key == "q":
            self._direc="OUEST"
        if key == "z":
            self._direc="NORD"        
            

        

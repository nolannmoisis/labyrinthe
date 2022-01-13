from Labyrinthe import *
from Robot import *

global MonLaby
global MonRobot

def setup():
    global MonLaby
    global MonRobot
    
    size (400, 400)
    
    MonLaby = Labyrinthe()
    println(MonLaby._carteLaby)
    
    MonRobot = robot(MonLaby._entreeX,MonLaby._entreeY,"OUEST")
    println(MonRobot._posX)
    println(MonRobot._posY)
    println(MonRobot._direc)
    
def draw():
    global MonLaby
    global MonRobot
    background(255,255,255)
    MonLaby.dessin()
    MonRobot.dessin()
    MonRobot.bouge()
    if MonRobot._posX == MonLaby._sortieX and MonRobot._posY == MonLaby._sortieY:
        text("Victoire!!!,Vous avez gagne!!!",120,200)
    pass
    
def keyReleased():
    if MonRobot._posX != MonLaby._sortieX or MonRobot._posY != MonLaby._sortieY:
        if key == "d":
            if MonLaby._carteLaby[MonRobot._posY][MonRobot._posX + 1] != '1':
                MonRobot._posX=MonRobot._posX + 1
                    
        if key == "z":
            if MonLaby._carteLaby[MonRobot._posY - 1][MonRobot._posX] != '1':
                MonRobot._posY=MonRobot._posY - 1
                    
        if key == "q":
            if MonLaby._carteLaby[MonRobot._posY][MonRobot._posX - 1] != '1':
                MonRobot._posX=MonRobot._posX - 1
                    
        if key == "s":
            if MonLaby._carteLaby[MonRobot._posY + 1][MonRobot._posX] != '1':
                MonRobot._posY=MonRobot._posY + 1
    
    
    
    

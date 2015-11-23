'''
ALL SPRITES IN THIS GAME HAVE SOME COMMON FUNCTIONS, DEFINED IN THIS ABSTRACT CLASS
Use abc module of python to create abstract classes.
http://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python
**I'll just use inheritance without abstraction
'''
#https://docs.python.org/3/library/abc.html

#from abc import ABCMeta, abstractmethod
from Globals import *

class AbstractSprite(object):
    def __init__(self):
         self.position = None
         self.velocity = None
         self.graphic = None
         self.radius = None
         
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        
    def create(self, graphic, radius):
        self.graphic = graphic
        self.radius = radius
        
    def destroy(self):
        global sprites
        global enemies
        sprites.remove(self)
        enemies.remove(self)
        
    def update(self):
        global player
        if self != player:
            if isRightBound(self) or isLeftBound(self):
                velocity = PVector(-1 * velocity.x, 0)
        self.position.add(self.velocity)
        
    def display(self):
        shape(self.graphic, self.position.x, self.position.y)
        
    def updateAndDisplay(self):
        self.update()
        self.display()
        
    def isColliding(a, b):
        dx = a.position.x - b.position.x
        dy = a.position.y - b.position.y
        rr = a.radius + b.radius
        if dx * dx + dy * dy < rr * rr:
            return True
        else:
            return False
from AbstractSprite import *

class HostileSprite(AbstractSprite):
    def __init__(self, team, radius, graphic, position, velocity):
        AbstractSprite.__init__(self, position, velocity)
        self.shotTime = 0
        self.fireDelay = 300
        self.team = team
        
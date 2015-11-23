from ShapeFactory import *
from HostileSprite import *

'''
GLOBAL VARIABLES
'''
playersTeam = 1
enemiesTeam = 2
playerLives = 3
playerSpeedLimit = 8
enemySpeedLimit = 4
stage = 0
invincible = False
lockedControls = True
keys = []
sprites = []
enemies = []
levels = []

currentLevel = None
factory = None
player = None
playerControllerLine = None
lifeIcon = None

'''
SETUP - INITIALIZE, RUNS ONCE
this method is built into processing. it is always called one time
'''
def setup():
    noCursor()
    fullScreen(P2D)
    
    global factory, player, lifeIcon, currentLevel
    factory = ShapeFactory()
    lifeIcon = factory.basicPlayer.getChild(0) #the chassis
    player = spawnPlayer()
    playerControllerLine = 0.85 * height
    
    sprites.append(player)
    enemies.append(player)
    
'''    
DRAW - THE MAIN DRAWING LOOP REPEATS EVERY FRAME
this method is build into processing. it is called repeatedly as a loop
'''
def draw():
    background(25)
    showPlayerLives()
    if playerLives == 0:
        endGame("lose")
        
    for i in range(len(sprites)):
        sprites[i].updateAndDisplay()
        
'''
DISPLAY LIVES AS A PLAYER SHAPE, BOTTOM LEFT
'''                    
def showPlayerLives():
    for i in range(playerLives):
        shape(lifeIcon, 60 + i * 100, height - 40)

'''
CHECKS THE STATE OF THE GAME (WIN OR LOSE), DISPLAY A MESSAGE, STOP THE GAME LOOP
'''                
def endGame(condition):
    if condition == "lose":
        cursor();
        textAlign(CENTER);
        textSize(48);
        text("Game Over", width/2, height/2);
        noLoop();
    elif condition == "win":
        cursor();
        textAlign(CENTER);
        textSize(48);
        text("You Beat the Game", width/2, height/2);
        noLoop();
        
'''
SPAWN A NEW PLAYER
'''
def spawnPlayer():
    startingPosition = PVector(0.5 * width, 0.85 * height)
    initialVelocity = PVector(0, 0)
    graphic = factory.basicPlayer
    radius = factory.basicPlayerRadius
    return HostileSprite(playersTeam, radius, graphic, startingPosition, initialVelocity);

def isLeftBound(sprite):
    leftBoundary = 2 * sprite.radius
    if sprite.position.x <= leftBoundary:
        return True
    else:
        return False
    
def isRightBound(sprite):
    rightBoundary = width - 2 * sprite.radius
    if sprite.position.x >= rightBoundary:
        return True
    else:
        return False
    
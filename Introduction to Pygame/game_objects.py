import pygame
import random
pygame.init()

# Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
WIDTH = 1000 
HEIGHT = 500
DISPLAYWINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
DISPLAYWINDOW_LEFT, DISPLAYWINDOW_RIGHT, DISPLAYWINDOW_TOP, DISPLAYWINDOW_BOTTOM = 0, 1000, 0, 500

# Game Settings
pygame.display.set_caption('Hello Pygame')
clock = pygame.time.Clock()

# Declaring Game Objects
class Player:
    def __init__(self):
        self.WIDTH = 20
        self.HEIGHT = 20
        self.bodyLength = 3
        self.headPositionX, self.headPositionY = 500, 260
        self.bodyPositions = [(500, 260), (500, 260), (500, 260)]
        self.velocityX, self.velocityY = 0, 0           
        self.direction = 'Rest'
        self.change_to = 'Rest'
    
    def move(self): 
        self.bodyPositions.insert(0, (self.headPositionX, self.headPositionY))  
        self.bodyPositions.pop()

        for playerBody in player.bodyPositions:
            pygame.draw.rect(DISPLAYWINDOW, WHITE, [playerBody[0], playerBody[1], self.WIDTH, self.HEIGHT])
    
    def head_collided_in_body(self):
        if (self.headPositionX, self.headPositionY) in self.bodyPositions and self.direction != 'Rest': 
            return True
        else: return False
    
    def head_collided_in_border(self):
        if (self.headPositionX < DISPLAYWINDOW_LEFT or self.headPositionX >= DISPLAYWINDOW_RIGHT) or\
            (self.headPositionY < DISPLAYWINDOW_TOP or self.headPositionY >= DISPLAYWINDOW_BOTTOM):
            return True
        else: return False

class Food:
    def __init__(self):
        self.WIDTH = 20
        self.HEIGHT = 20
        self.positionX = 0
        self.positionY = 0
        self.possiblePositions = [(positionX, positionY) for positionX in range(0,1000,20) for positionY in range(0,500,20) if (positionX, positionY) not in player.bodyPositions]
        self.randomize_position()

    def randomize_position(self):
        self.possiblePositions = [(positionX, positionY) for positionX in range(0,1000,20) for positionY in range(0,500,20) if (positionX, positionY) not in player.bodyPositions]
        self.randomChoice = random.choice(self.possiblePositions) 
        self.positionX = self.randomChoice[0]
        self.positionY = self.randomChoice[1]            

# Assigning Game Objects        
player = Player()
food = Food()





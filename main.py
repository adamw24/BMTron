import pygame
import numpy
import keyboard
import sys
from pygame.surface import Surface
from pygame.time import wait

BLACK = (0,0,0)
WHITE = (255,255,255)

#Constants
window_width = 800
window_height = 600
paddle_size = 150
paddle_offset = 30
paddle_thickness = 10
paddle_start_position = (window_height - paddle_size) /2

display_surf = pygame.display.set_mode((window_width,window_height))

#Main Function.
def main():
    pygame.init()
    global display_surf
    display_surf = pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('bmtron')
    drawBackground()

def drawBackground():
    display_surf.fill((0,0,0))

pasttrail = []

class player():
    def __init__ (self, x, y, dir, color):
        self.x = x
        self.y = y
        self.direction = dir
        self.color = color
        self.alive = True
    
    def draw(self):
        pygame.draw.circle(display_surf, self.color, (self.x,self.y), 1, 1)
        pasttrail.append((self.x,self.y))
    
    def move(self):
        if abs(self.direction) == 1:
            self.y += self.direction
        else:
            self.x += self.direction/2
        if((self.x,self.y) in pasttrail):
            print("collide")
            self.alive = False
        self.draw()

        

    def changeDirection(self, newD):
        self.direction = newD


drawBackground()
playerset = {}
playerOne = player(20,20,2,(0,0,255))
playerTwo = player(window_width-20,window_height-20,-2,(255,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keyboard.is_pressed("q"):
            pygame.quit()
            sys.exit()
    if(playerOne.alive and playerTwo.alive):
        playerOne.move()
        playerTwo.move()
        if keyboard.is_pressed('w'):
            playerOne.changeDirection(-1)
        if keyboard.is_pressed('d'):
            playerOne.changeDirection(2)
        if keyboard.is_pressed('s'):
            playerOne.changeDirection(1)
        if keyboard.is_pressed('a'):
            playerOne.changeDirection(-2)

        if keyboard.is_pressed('i'):
            playerTwo.changeDirection(-1)
        if keyboard.is_pressed('l'):
            playerTwo.changeDirection(2)
        if keyboard.is_pressed('k'):
            playerTwo.changeDirection(1)
        if keyboard.is_pressed('j'):
            playerTwo.changeDirection(-2)
        wait(5)
    pygame.display.flip()


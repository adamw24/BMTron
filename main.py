import pygame
import numpy
import keyboard
import sys
from pygame.surface import Surface
from pygame.time import wait

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

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
    display_surf.fill((0,0,0))

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
        if((self.x,self.y) in pasttrail or not self.withinBounds()):
            print("Game Over")
            self.alive = False
        else:
            self.draw()
        
    def withinBounds(self):
        return self.x > 1 and self.x < window_width -1 and self.y > 1 and self.y < window_height -1

    def changeDirection(self, newD):
        self.direction = newD

offset = 150
pasttrail = []
playerOne = player(offset,offset,2,GREEN)
playerTwo = player(window_width-offset,window_height-offset,-2,RED)
pygame.draw.rect(display_surf, WHITE, ((0,0),(window_width,window_height)), 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keyboard.is_pressed("q"):
            pygame.quit()
            sys.exit()
    if(playerOne.alive and playerTwo.alive):
        playerOne.move()
        playerTwo.move()
        if keyboard.is_pressed('w') and playerOne.direction != 1:
            playerOne.changeDirection(-1)
        if keyboard.is_pressed('d') and playerOne.direction != -2:
            playerOne.changeDirection(2)
        if keyboard.is_pressed('s') and playerOne.direction != -1:
            playerOne.changeDirection(1)
        if keyboard.is_pressed('a') and playerOne.direction != 2:
            playerOne.changeDirection(-2)

        if keyboard.is_pressed('i') and playerTwo.direction != 1:
            playerTwo.changeDirection(-1)
        if keyboard.is_pressed('l') and playerTwo.direction != -2:
            playerTwo.changeDirection(2)
        if keyboard.is_pressed('k') and playerTwo.direction != -1:
            playerTwo.changeDirection(1)
        if keyboard.is_pressed('j') and playerTwo.direction != 2:
            playerTwo.changeDirection(-2)
        wait(5)
    if keyboard.is_pressed('r'):
        pasttrail.clear()
        playerOne = player(offset,offset,2,GREEN)
        playerTwo = player(window_width-offset,window_height-offset,-2,RED)
        display_surf.fill(BLACK)
        pygame.draw.rect(display_surf, WHITE, ((0,0),(window_width,window_height)), 1)

    pygame.display.update()

if __name__=='__main__':
    main()

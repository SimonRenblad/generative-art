#!/usr/bin/env python2

import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerSprite, self).__init__()
        self.surf = pygame.Surface((75,75))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.image = self.surf

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Cell, self).__init__()
        self.x = x
        self.y = y
        self.width = 5
        self.height = 5
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(WHITE)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = self.surf

    def update(self):
        pass

    def translate(self, x, y):
        self.rect.move_ip(x, y)
        self.x = self.x + x
        self.y = self.y + y

    def teleport(self, x, y):
        self.rect.move_ip(x - self.x, y - self.y)
        self.x = x
        self.y = y


WIDTH = 360
HEIGHT = 480
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animations")
clock = pygame.time.Clock()     ## For syncing the FPS


## group all the sprites together for ease of update
player = PlayerSprite()
cell = Cell(0,0)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(cell)

## Game loop
running = True
key_pressed = None
pygame.time.set_timer(pygame.USEREVENT, 500)
while running:
    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            cell.translate(5,5)

    pressed_keys = pygame.key.get_pressed()


    #2 Update
    #all_sprites.update()
    player.update(pressed_keys)

    #3 Draw/render
    screen.fill(BLACK)

    

    all_sprites.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()



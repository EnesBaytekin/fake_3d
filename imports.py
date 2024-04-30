import pygame
import pygame.display
import pygame.event
import pygame.image
import pygame.key
import pygame.mouse
import pygame.draw
import pygame.transform
from pygame import Vector2
from time import time
from math import degrees,radians,sin,cos

from input import Input
INPUT = Input()

SIZE = (480,270)

BG_TILE1 = pygame.Surface((16,16))
BG_TILE1.fill((63,238,155))
for i in range(2):
    pygame.draw.rect(BG_TILE1,(36,203,124),(i*8,i*8,8,8))

BG1 = pygame.Surface(SIZE)
for x in range(SIZE[0]//16+1):
    for y in range(SIZE[1]//16+1):
        BG1.blit(BG_TILE1,(x*16,y*16))

def import_stack(file_name:str):
    image = pygame.image.load(file_name).convert_alpha()
    w,h = image.get_width(),image.get_height()
    size = h
    count = w//h
    stack = []
    for i in range(count):
        layer = pygame.Surface((size,size),pygame.SRCALPHA)
        layer.blit(image,(0,0),(i*size,0,size,size))
        stack.append(layer)
        stack.append(layer)
    return stack

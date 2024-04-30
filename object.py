from imports import *
from camera import Camera

class Object:
    def __init__(self,pos:Vector2):
        self.pos = Vector2(pos)
        self.image_stack = import_stack("stack2.png")
    def draw(self,surface:pygame.Surface,camera:Camera,origin:Vector2):
        for i,layer in enumerate(self.image_stack):
            pos = origin+self.pos+camera.up*i*camera.pitch*0.8
            surface.blit(layer,(int(pos.x),int(pos.y)))

from imports import *
from camera import Camera
from object import Object

class Game:
    def __init__(self):
        self.objects = [
            Object((0,0)),
            Object((0,256)),
            Object((64,192)),
            Object((-128,128)),
        ]
        self.camera = Camera()
    def draw(self,screen:pygame.Surface):
        display = pygame.Surface((SIZE[0]*3,SIZE[1]*3),pygame.SRCALPHA)
        for x in range(3):
            for y in range(3):
                display.blit(BG1,(x*SIZE[0],y*SIZE[1]))
        
        # pygame.draw.circle(display,(88,33,33),(SIZE[0]*3//2,SIZE[1]*3//2),16)
        # pygame.draw.circle(display,(156,48,185),(SIZE[0]*3//2,SIZE[1]+64),8)
        # pygame.draw.rect(display,(156,123,185),(SIZE[0]+160,SIZE[1]+64,20,8))
        
        for obj in self.objects:
            obj.draw(display,self.camera,Vector2(SIZE)*3/2)

        display = pygame.transform.rotate(display,self.camera.angle)
        display = pygame.transform.scale(display,(int(display.get_width()),int(display.get_height()/self.camera.pitch)))

        screen.fill((0,0,0))
        screen.blit(display,(SIZE[0]//2-display.get_width()//2,SIZE[1]//2-display.get_height()//2+int(SIZE[1]*(1-1/self.camera.pitch)*0.5)))

        pygame.display.flip()
    def update(self,dt:float):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        INPUT.update()
        self.camera.update(dt)
        return True

from imports import *

class Camera:
    def __init__(self):
        self.pos = Vector2(0,0)

        self.angle = 0
        self.angle_to = self.angle

        self.pitch = 1.0
        self.pitch_min = 1
        self.pitch_max = 2
        self.pitch_to = self.pitch

        angle = radians(-self.angle+90)
        self.up = Vector2(cos(angle),sin(angle))
    def update(self,dt):
        if INPUT.mouse_check_button(0):
            mouse_x, mouse_y = INPUT.get_mouse_pos()
            self.pitch_to += -(SIZE[1]*0.5-mouse_y)*0.01
            self.angle_to += -(SIZE[0]*0.5-mouse_x)*0.1
        pygame.mouse.set_pos(SIZE[0]//2,SIZE[1]//2)
        dx = INPUT.keyboard_check(pygame.K_RIGHT)-INPUT.keyboard_check(pygame.K_LEFT)
        dy = INPUT.keyboard_check(pygame.K_UP)-INPUT.keyboard_check(pygame.K_DOWN)
        if dy != 0 or dx != 0:
            self.pitch_to
        self.pitch_to = min(max(self.pitch_to,self.pitch_min),self.pitch_max)
        self.pitch += (self.pitch_to-self.pitch)*0.1
        self.angle += (self.angle_to-self.angle)*0.1
        angle = radians(self.angle-90)
        self.up = Vector2(cos(angle),sin(angle))

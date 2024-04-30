import pygame
import pygame.key
import pygame.mouse
from pygame import Vector2

class Input:
    def __init__(self):
        self._mouse_pos = Vector2(0,0)
        self._last_mouse_pos = Vector2(0,0)

        self._mouse_buttons = None
        self._last_mouse_buttons = None
        self._keys = None
        self._last_keys = None
    
    def get_mouse_pos(self):
        return self._mouse_pos
    def get_mouse_last_pos(self):
        return self._last_mouse_pos
    def get_mouse_motion(self):
        return self._mouse_pos-self._last_mouse_pos
    
    def mouse_check_button(self,button_id:int):
        return self._mouse_buttons[button_id]
    def mouse_check_button_pressed(self,button_id:int):
        return not self._last_mouse_buttons[button_id] and self._mouse_buttons[button_id]
    def mouse_check_button_released(self,button_id:int):
        return self._last_mouse_buttons[button_id] and not self._mouse_buttons[button_id]

    def keyboard_check(self,key:int):
        return self._keys[key]
    def keyboard_check_pressed(self,key:int):
        return not self._last_keys[key] and self._keys[key]
    def keyboard_check_released(self,key:int):
        return self._last_keys[key] and not self._keys[key]

    def update(self):
        mx,my = pygame.mouse.get_pos()
        self._last_mouse_pos = self._mouse_pos.xy
        self._mouse_pos = Vector2(mx,my)

        self._last_mouse_buttons = self._mouse_buttons
        self._mouse_buttons = pygame.mouse.get_pressed()

        self._last_keys = self._keys
        self._keys = pygame.key.get_pressed()

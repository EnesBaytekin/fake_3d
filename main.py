from imports import *
from game import Game

class Window:
    def __init__(self,size:tuple):
        self.size = size
        self.screen = pygame.display.set_mode(self.size,pygame.SCALED|pygame.FULLSCREEN)
        self.game = Game()
        self.running = False
    def mainloop(self):
        self.running = True
        last_time = time()
        current_time = time()
        pygame.mouse.set_visible(False)
        while self.running:
            current_time = time()
            delta_time = current_time-last_time
            last_time = current_time
            if delta_time != 0: print(1/delta_time)
            if self.game.update(delta_time):
                self.game.draw(self.screen)
            else:
                self.running = False
            
if __name__ == "__main__":
    window = Window(SIZE)
    window.mainloop()
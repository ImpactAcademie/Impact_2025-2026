from time import time

import pygame


class Animation:
    def __init__(self, path, nb, fps):
        self.path = path
        self.nb = nb
        self.fps = fps
        self.start_time = None
        self.current = 0
        self.images = [pygame.image.load(path+str(i+1)+".png") for i in range(nb)]

    def start(self):
        self.start_time = time()

    def pause(self):
        pass

    def stop(self):
        self.start_time = None

    def update(self):
        if self.start_time == None:
            return
        self.current = int((time()-self.start_time)/self.fps)%self.nb

    def draw(self, screen, pos):
        screen.blit(self.images[self.current], pos)
        
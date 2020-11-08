import os
import time
import pygame.mixer

pygame.mixer.init()

click = pygame.mixer.Sound(os.path.join("res", "sounds", "click.ogg"))
select = pygame.mixer.Sound(os.path.join("res", "sounds", "select.ogg"))
roll = pygame.mixer.Sound(os.path.join("res", "sounds", "roll.ogg"))

background = pygame.mixer.Sound(os.path.join("res", "sounds", "background.ogg"))

playable = True

class Music:
    def __init__(self):
        self.playing = False
        
    def play(self, load):
        if load[0]:
            background.play(-1)
            self.playing = True
    
    def stop(self):
        background.stop()
        self.playing = False
        
    def is_playing(self):
        return self.playing

def play_click(load):
    if load[0]:
        click.play()
        time.sleep(0.1)
    
def play_roll(load):
    if load[0]:
        roll.play()
    
def play_select(load):
    if load[0]:
        select.play()
        time.sleep(0.1)
    
        
pygame.mixer.quit()
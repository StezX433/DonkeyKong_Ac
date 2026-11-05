import os
import random
import pygame

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

info = pygame.display.Info()
screen_width , screen_height = info.current_w , info.current_h
window_width , window_height = screen_width - 800 , screen_height - 150


timer = pygame.time.Clock()
fps = 60
pygame.display.set_caption('DonkeyKong by Kshitij')

screen = pygame.display.set_mode([window_width,window_height])

section_width = window_width // 32
section_height = window_height // 32
slope = section_height // 8


run = True
while run:
    screen.fill('black')
    timer.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()





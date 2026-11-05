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


class Bridge:
    def __init__(self , x_pos , y_pos , length):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.top = self.draw()
        
    def draw(self):
        line_width = 7
        platform_color = (225, 51, 129)

        for i in range(self.length):
            bot_coord = self.y_pos + section_height
            left_coord = self.x_pos + (section_width * i)
            mid_coord = left_coord + (section_width * 0.5)
            right_coord = left_coord + section_width
            top_coord = self.y_pos

            pygame.draw.line(
                screen, platform_color,
                (left_coord, top_coord),
                (right_coord, top_coord),
                line_width
            )

            pygame.draw.line(
                screen, platform_color,
                (left_coord, bot_coord),
                (right_coord, bot_coord),
                line_width
            )

            pygame.draw.line(
                screen, platform_color,
                (left_coord, bot_coord),
                (mid_coord, top_coord),
                line_width
            )

            pygame.draw.line(
                screen, platform_color,
                (mid_coord, top_coord),
                (right_coord, bot_coord),
                line_width
            )
        top_line = pygame.rect.Rect(
            (self.x_pos, self.y_pos),
            (self.length * section_width, 2)
        )

        # pygame.draw.rect(screen, 'blue', top_line)

        return top_line
    
    
    
#function to draw ladders and platforms
def draw_screen():
    bridges_list = [(2,500,5)]
    bridge_objs = []
    ladders_list = [] 
    
    for bridge in bridges_list:
        bridge_objs.append(Bridge(*bridge))
        
        
        
    



run = True
while run:
    screen.fill('black')
    timer.tick(fps)
    
    #draw platforms and ladder on to the screen using dedicated functions
    draw_screen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()





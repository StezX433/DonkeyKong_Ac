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


barrel_spawn_time = 360
barrel_count = barrel_spawn_time / 2
barrel_time = 360
barrel_img = pygame.transform.scale(
    pygame.image.load('assets/images/barrels/barrel.png'),
    (section_width * 1.5, section_height * 2)
)
flames_img = pygame.transform.scale(pygame.image.load('assets/images/fire.png'),
                                    (section_width * 2, section_height))
barrel_side = pygame.transform.scale(pygame.image.load('assets/images/barrels/barrel2.png'),
                                     (section_width * 2, section_height * 2.5))
dk1 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk1.png'),
                             (section_width * 5, section_height * 5))
dk2 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk2.png'),
                             (section_width * 5, section_height * 5))
dk3 = pygame.transform.scale(pygame.image.load('assets/images/dk/dk3.png'),
                             (section_width * 5, section_height * 5))
peach1 = pygame.transform.scale(pygame.image.load('assets/images/peach/peach1.png'),
                                (2 * section_width, 3 * section_height))
peach2 = pygame.transform.scale(pygame.image.load('assets/images/peach/peach2.png'),
                                (2 * section_width, 3 * section_height))
fireball = pygame.transform.scale(pygame.image.load('assets/images/fireball.png'),
                                  (1.5 * section_width, 2 * section_height))
fireball2 = pygame.transform.scale(pygame.image.load('assets/images/fireball2.png'),
                                   (1.5 * section_width, 2 * section_height))
hammer = pygame.transform.scale(pygame.image.load('assets/images/hammer.png'),
                                   (2 * section_width, 2 * section_height))
standing = pygame.transform.scale(pygame.image.load('assets/images/mario/standing.png'),
                                  (2 * section_width, 2.5 * section_height))
jumping = pygame.transform.scale(pygame.image.load('assets/images/mario/jumping.png'),
                                 (2 * section_width, 2.5 * section_height))
running = pygame.transform.scale(pygame.image.load('assets/images/mario/running.png'),
                                 (2 * section_width, 2.5 * section_height))
climbing1 = pygame.transform.scale(pygame.image.load('assets/images/mario/climbing1.png'),
                                   (2 * section_width, 2.5 * section_height))
climbing2 = pygame.transform.scale(pygame.image.load('assets/images/mario/climbing2.png'),
                                   (2 * section_width, 2.5 * section_height))
hammer_stand = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_stand.png'),
                                      (2.5 * section_width, 2.5 * section_height))
hammer_jump = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_jump.png'),
                                     (2.5 * section_width, 2.5 * section_height))
hammer_overhead = pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_overhead.png'),
                                         (2.5 * section_width, 3.5 * section_height))

start_y = window_height - 2 * section_height

row2_y = start_y - 4 * section_height
row3_y = row2_y - 7 * slope - 3 * section_height
row4_y = row3_y - 4 * section_height
row5_y = row4_y - 7 * slope - 3 * section_height
row6_y = row5_y - 4 * section_height

row6_top = row6_y - 4 * slope
row5_top = row5_y - 8 * slope
row4_top = row4_y - 8 * slope
row3_top = row3_y - 8 * slope
row2_top = row2_y - 8 * slope
row1_top = start_y - 5 * slope
fireball_trigger = False
active_level = 0


levels = [{'bridges': [(1, start_y, 15), (16, start_y - slope, 3),
                       (19, start_y - 2 * slope, 3), (22, start_y - 3 * slope, 3),
                       (25, start_y - 4 * slope, 3), (28, start_y - 5 * slope, 3),
                       (25, row2_y, 3), (22, row2_y - slope, 3),
                       (19, row2_y - 2 * slope, 3), (16, row2_y - 3 * slope, 3),
                       (13, row2_y - 4 * slope, 3), (10, row2_y - 5 * slope, 3),
                       (7, row2_y - 6 * slope, 3), (4, row2_y - 7 * slope, 3),
                       (2, row2_y - 8 * slope, 2), (4, row3_y, 3),
                       (7, row3_y - slope, 3), (10, row3_y - 2 * slope, 3),
                       (13, row3_y - 3 * slope, 3), (16, row3_y - 4 * slope, 3),
                       (19, row3_y - 5 * slope, 3), (22, row3_y - 6 * slope, 3),
                       (25, row3_y - 7 * slope, 3), (28, row3_y - 8 * slope, 2),
                       (25, row4_y, 3), (22, row4_y - slope, 3),
                       (19, row4_y - 2 * slope, 3), (16, row4_y - 3 * slope, 3),
                       (13, row4_y - 4 * slope, 3), (10, row4_y - 5 * slope, 3),
                       (7, row4_y - 6 * slope, 3), (4, row4_y - 7 * slope, 3),
                       (2, row4_y - 8 * slope, 2), (4, row5_y, 3),
                       (7, row5_y - slope, 3), (10, row5_y - 2 * slope, 3),
                       (13, row5_y - 3 * slope, 3), (16, row5_y - 4 * slope, 3),
                       (19, row5_y - 5 * slope, 3), (22, row5_y - 6 * slope, 3),
                       (25, row5_y - 7 * slope, 3), (28, row5_y - 8 * slope, 2),
                       (25, row6_y, 3), (22, row6_y - slope, 3),
                       (19, row6_y - 2 * slope, 3), (16, row6_y - 3 * slope, 3),
                       (2, row6_y - 4 * slope, 14), (13, row6_y - 4 * section_height, 6),
                       (10, row6_y - 3 * section_height, 3)],
           'ladders': [(12, row2_y + 6 * slope, 2), (12, row2_y + 26 * slope, 2),
                       (25, row2_y + 11 * slope, 4), (6, row3_y + 11 * slope, 3),
                       (14, row3_y + 8 * slope, 4), (10, row4_y + 6 * slope, 1),
                       (10, row4_y + 24 * slope, 2), (16, row4_y + 6 * slope, 5),
                       (25, row4_y + 9 * slope, 4), (6, row5_y + 11 * slope, 3),
                       (11, row5_y + 8 * slope, 4), (23, row5_y + 4 * slope, 1),
                       (23, row5_y + 24 * slope, 2), (25, row6_y + 9 * slope, 4),
                       (13, row6_y + 5 * slope, 2), (13, row6_y + 25 * slope, 2),
                       (18, row6_y - 27 * slope, 4), (12, row6_y - 17 * slope, 2),
                       (10, row6_y - 17 * slope, 2), (12, -5, 13), (10, -5, 13)],
          'hammers': [(4, row6_top + section_height), (4, row4_top+section_height)],
           'target': (13, row6_y - 4 * section_height, 3)}]

# barrels class
class Barrel(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)

        self.y_change = 0
        self.x_change = 1
        self.pos = 0
        self.count = 0
        self.oil_collision = False
        self.falling = False
        self.check_lad = False
        self.bottom = self.rect

    def draw(self):
        screen.blit(
            pygame.transform.rotate(barrel_img, 90 * self.pos),
            self.rect.topleft
        )
        
    def update(self, fire_trig):
        if self.y_change < 8 and not self.falling:
            barrel.y_change += 2

        for i in range(len(plats)):
            if self.bottom.colliderect(plats[i]):
                self.y_change = 0
                self.falling = False

        if self.rect.colliderect(oil_drum):
            if not self.oil_collision:
                self.oil_collision = True
                if random.randint(0, 4) == 4:
                    fire_trig = True

        if not self.falling:
            if row5_top >= self.rect.bottom or row3_top >= self.rect.bottom >= row4_top or row1_top >= self.rect.bottom:
                self.x_change = 3
            else:
                self.x_change = -3
        else:
            self.x_change = 0
            
        return fire_trig
    def check_fall(self):
        already_collided = False

        below = pygame.rect.Rect(
            (self.rect[0], self.rect[1] + section_height),
            (self.rect[2], section_height)
        )

        for lad in lads:
            if below.colliderect(lad) and not self.falling and not self.check_lad:
                self.check_lad = True
                already_collided = True

                if random.randint(0, 60) == 60:
                    self.falling = True
                    self.y_change = 4

        if not already_collided:
            self.check_lad = False

    def draw(self):
        screen.blit(
            pygame.transform.rotate(barrel_img, 90 * self.pos),
            self.rect.topleft
        )
        
    

#bridge class
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
    
#ladder class
class Ladder:
    def __init__(self,x_pos,y_pos,length):
        self.x_pos = x_pos * section_width
        self.y_pos = y_pos
        self.length = length
        self.body = self.draw()
        
    def draw(self):
        line_width = 3
        lad_color = 'light blue'
        lad_height = 0.6

        for i in range(self.length):
            top_coord = self.y_pos + lad_height * section_height * i
            bot_coord = top_coord + lad_height * section_height
            mid_coord = (lad_height / 2)*section_height + top_coord
            left_coord = self.x_pos
            right_coord = left_coord + section_width

            pygame.draw.line(
                screen, lad_color,
                (left_coord, top_coord),
                (left_coord, bot_coord),
                line_width
            )

            pygame.draw.line(
                screen, lad_color,
                (right_coord, top_coord),
                (right_coord, bot_coord),
                line_width
            )

            pygame.draw.line(
                screen, lad_color,
                (left_coord, mid_coord),
                (right_coord, mid_coord),
                line_width
            )

        body = pygame.rect.Rect(
            (self.x_pos, self.y_pos - section_height),
            (section_width, (lad_height * self.length + section_height))
        )

        return body
        
        
# function to draw platforms and ladders
def draw_screen():
    platforms = []
    climbers = []
    ladder_objs = []
    bridge_objs = []

    ladders = levels[active_level]['ladders']
    bridges = levels[active_level]['bridges']

    for ladder in ladders:
        ladder_objs.append(Ladder(*ladder))
        if ladder[2] >= 3:
            climbers.append(ladder_objs[-1].body)

    for bridge in bridges:
        bridge_objs.append(Bridge(*bridge))
        platforms.append(bridge_objs[-1].top)

    return platforms, climbers

#sprite class
barrels = pygame.sprite.Group()
oil_drum = pygame.rect.Rect((1,1),(1,1))

run = True
while run:
    screen.fill('black')
    timer.tick(fps)
    if barrel_count < barrel_spawn_time:
        barrel_count += 1

    else:
        barrel_count = random.randint(0, 120)
        barrel_time = barrel_count - barrel_spawn_time

        barrel = Barrel(270, 270)
        barrels.add(barrel)
    
    #draw platforms and ladder on to the screen using dedicated functions
    plats = draw_screen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
pygame.quit()





import pygame, sys
from pygame.locals import *

pygame.init()

# Set Screen Size
screen = pygame.display.set_mode((1366, 720))

# Change window text
pygame.display.set_caption('Project!')

# Add custom app icon
icon = pygame.image.load("Full Screen Cursor.png")
pygame.display.set_icon(icon)

# Font
font = pygame.font.SysFont('Constantia', 20)

# Window variables

window_count = 10

window_1  = pygame.Rect(28, 122, 240, 160)
window_2  = pygame.Rect(295, 122, 240, 160)
window_3  = pygame.Rect(563, 122, 240, 160)
window_4  = pygame.Rect(831, 122, 240, 160)
window_5  = pygame.Rect(1098, 122, 240, 160)
window_6  = pygame.Rect(28, 437, 240, 160)
window_7  = pygame.Rect(295, 437, 240, 160)
window_8  = pygame.Rect(563, 437, 240, 160)
window_9  = pygame.Rect(831, 437, 240, 160)
window_10 = pygame.Rect(1098, 437, 240, 160)

window_1_selected  = True
window_2_selected  = True
window_3_selected  = True
window_4_selected  = True
window_5_selected  = True
window_6_selected  = True
window_7_selected  = True
window_8_selected  = True
window_9_selected  = True
window_10_selected = True

# Next button variables
next_btn_clicked = False

#######################################################################################################################################################################

def window():
    
    if not window_1_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_1)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_1)

    if not window_2_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_2)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_2)

    if not window_3_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_3)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_3)

    if not window_4_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_4)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_4)

    if not window_5_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_5)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_5)

    if not window_6_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_6)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_6)

    if not window_7_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_7)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_7)

    if not window_8_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_8)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_8)

    if not window_9_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_9)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_9)

    if not window_10_selected:
        pygame.draw.rect(screen, (255, 0, 0), window_10)
    else:
        pygame.draw.rect(screen, (0, 255, 0), window_10)

#######################################################################################################################################################################

def window_clicked():
    global window_count
    
    if window_1.collidepoint(pos):
        global window_1_selected

        if window_1_selected:
            window_1_selected = False
            window_count -= 1
        else:
            window_1_selected = True
            window_count += 1

    if window_2.collidepoint(pos):
        global window_2_selected

        if window_2_selected:
            window_2_selected = False
            window_count -= 1
        else:
            window_2_selected = True
            window_count += 1

    if window_3.collidepoint(pos):
        global window_3_selected

        if window_3_selected:
            window_3_selected = False
            window_count -= 1
        else:
            window_3_selected = True
            window_count += 1

    if window_4.collidepoint(pos):
        global window_4_selected

        if window_4_selected:
            window_4_selected = False
            window_count -= 1
        else:
            window_4_selected = True
            window_count += 1

    if window_5.collidepoint(pos):
        global window_5_selected

        if window_5_selected:
            window_5_selected = False
            window_count -= 1
        else:
            window_5_selected = True
            window_count += 1

    if window_6.collidepoint(pos):
        global window_6_selected

        if window_6_selected:
            window_6_selected = False
            window_count -= 1
        else:
            window_6_selected = True
            window_count += 1

    if window_7.collidepoint(pos):
        global window_7_selected

        if window_7_selected:
            window_7_selected = False
            window_count -= 1
        else:
            window_7_selected = True
            window_count += 1

    if window_8.collidepoint(pos):
        global window_8_selected

        if window_8_selected:
            window_8_selected = False
            window_count -= 1
        else:
            window_8_selected = True
            window_count += 1

    if window_9.collidepoint(pos):
        global window_9_selected

        if window_9_selected:
            window_9_selected = False
            window_count -= 1
        else:
            window_9_selected = True
            window_count += 1

    if window_10.collidepoint(pos):
        global window_10_selected

        if window_10_selected:
            window_10_selected = False
            window_count -= 1
        else:
            window_10_selected = True
            window_count += 1

#######################################################################################################################################################################

def hover():
    
    if window_1.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_1, 2)

    if window_2.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_2, 2)

    if window_3.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_3, 2)

    if window_4.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_4, 2)

    if window_5.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_5, 2)

    if window_6.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_6, 2)

    if window_7.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_7, 2)

    if window_8.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_8, 2)

    if window_9.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_9, 2)

    if window_10.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (0, 0, 0), window_10, 2)

#######################################################################################################################################################################

class next_btn():
    
    next_btn_bg = (13, 110, 253)
    next_btn_bg_hover = (11, 94, 215)
    next_btn_bg_clicked = (10, 88, 202)
    next_btn_text = (255, 255, 255)
    width = 80
    height = 50
    
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_next_btn(self):
        
        global next_btn_clicked
        action = False
        
        pos = pygame.mouse.get_pos()
        next_btn = Rect(self.x, self.y, self.width, self.height)

        if next_btn.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and next_btn_clicked == False:
                next_btn_clicked = True
                pygame.draw.rect(screen, self.next_btn_bg_clicked, next_btn)
                
            elif pygame.mouse.get_pressed()[0] == 0 and next_btn_clicked == True:
                next_btn_clicked = False
                action = True
                pygame.draw.rect(screen, self.next_btn_bg_hover, next_btn)
		
            else:
                pygame.draw.rect(screen, self.next_btn_bg_hover, next_btn)
		
        else:
            pygame.draw.rect(screen, self.next_btn_bg, next_btn)

        #add shading to button
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        #add text to button
        text_img = font.render(self.text, True, self.next_btn_text)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

#######################################################################################################################################################################

def selected_windows():
    
    if window_count == 1:
        pygame.draw.rect(screen, (0, 255, 0), window_1)

    if window_count == 2:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)

    if window_count == 3:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)

    if window_count == 4:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)
        pygame.draw.rect(screen, (0, 255, 0), window_4)

    if window_count == 5:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)
        pygame.draw.rect(screen, (0, 255, 0), window_4)
        pygame.draw.rect(screen, (0, 255, 0), window_5)

    if window_count == 6:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)
        pygame.draw.rect(screen, (0, 255, 0), window_4)
        pygame.draw.rect(screen, (0, 255, 0), window_5)
        pygame.draw.rect(screen, (0, 255, 0), window_6)

    if window_count == 7:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)
        pygame.draw.rect(screen, (0, 255, 0), window_4)
        pygame.draw.rect(screen, (0, 255, 0), window_5)
        pygame.draw.rect(screen, (0, 255, 0), window_6)
        pygame.draw.rect(screen, (0, 255, 0), window_7)

    if window_count == 8:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)
        pygame.draw.rect(screen, (0, 255, 0), window_4)
        pygame.draw.rect(screen, (0, 255, 0), window_5)
        pygame.draw.rect(screen, (0, 255, 0), window_6)
        pygame.draw.rect(screen, (0, 255, 0), window_7)
        pygame.draw.rect(screen, (0, 255, 0), window_8)

    if window_count == 9:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)
        pygame.draw.rect(screen, (0, 255, 0), window_4)
        pygame.draw.rect(screen, (0, 255, 0), window_5)
        pygame.draw.rect(screen, (0, 255, 0), window_6)
        pygame.draw.rect(screen, (0, 255, 0), window_7)
        pygame.draw.rect(screen, (0, 255, 0), window_8)
        pygame.draw.rect(screen, (0, 255, 0), window_9)

    if window_count == 10:
        pygame.draw.rect(screen, (0, 255, 0), window_1)
        pygame.draw.rect(screen, (0, 255, 0), window_2)
        pygame.draw.rect(screen, (0, 255, 0), window_3)
        pygame.draw.rect(screen, (0, 255, 0), window_4)
        pygame.draw.rect(screen, (0, 255, 0), window_5)
        pygame.draw.rect(screen, (0, 255, 0), window_6)
        pygame.draw.rect(screen, (0, 255, 0), window_7)
        pygame.draw.rect(screen, (0, 255, 0), window_8)
        pygame.draw.rect(screen, (0, 255, 0), window_9)
        pygame.draw.rect(screen, (0, 255, 0), window_10)

#######################################################################################################################################################################

def next_screen():
    
    pygame.display.set_caption('Next')
    
    while True:

        for event in pygame.event.get():

            screen.fill((255, 255, 255))
            selected_windows()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

#######################################################################################################################################################################

while True:
    next = next_btn(1255, 625, 'Next')
    
    for event in pygame.event.get():

        screen.fill((255, 255, 255)) #Change screen color
        window()
        hover()

        if next.draw_next_btn():
            next_screen()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            window_clicked()

    pygame.display.update()

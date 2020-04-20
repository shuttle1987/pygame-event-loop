"""Experimenting with updates from outside the pygame loop"""

import threading

import pygame
import pygame.freetype


pygame.init()

UPDATE_FROM_TERMINAL = pygame.USEREVENT + 1

FONT = pygame.freetype.SysFont("Arial", 48)

font_coords = [40, 300]

text = "Hello world!"

COLOR_WHITE = (255, 255, 255)

screen_resolution = (1024, 768)
screen = pygame.display.set_mode(size=screen_resolution)

def text_changer():
    while True:
        new_text = input("New text:")
        evt = pygame.event.Event(UPDATE_FROM_TERMINAL, text=new_text)
        pygame.event.post(evt)

text_update_thread = threading.Thread(target=text_changer)
text_update_thread.start()

while True:
    for event in pygame.event.get():
        screen.fill(COLOR_WHITE)
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                font_coords[1] -= 10
            elif event.key == pygame.K_DOWN:
                font_coords[1] += 10
            elif event.key == pygame.K_LEFT:
                font_coords[0] -= 10
            elif event.key == pygame.K_RIGHT:
                font_coords[0] += 10
        if event.type == UPDATE_FROM_TERMINAL:
            text = event.text
        FONT.render_to(surf=screen, dest=font_coords, text=text, fgcolor=(128, 255, 255))
        pygame.display.flip()

text_update_thread.join()
pygame.quit()
import pygame
import pygame.freetype


pygame.init()

FONT = pygame.freetype.SysFont("Arial", 48)

font_coords = [40, 300]

text = "Hello world!"

COLOR_WHITE = (255, 255, 255)

screen_resolution = (1024, 768)
screen = pygame.display.set_mode(size=screen_resolution)

while True:
    screen.fill(COLOR_WHITE)
    for event in pygame.event.get():
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
        print(font_coords)
        FONT.render_to(surf=screen, dest=font_coords, text=text, fgcolor=(128, 255, 255))
        pygame.display.flip()

pygame.quit()
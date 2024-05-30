import pygame
from sys import exit

BLACK_COLOR = (0, 0 ,0)

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((550, 720))  # width, height

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        window.fill(BLACK_COLOR)
        clock.tick(60)
        pygame.display.flip()

main()
import pygame
import elements

window_height = 720
window_width = 550
window = pygame.display.set_mode((window_width, window_height))

ground = elements.Ground(window_width)
obstacles = []
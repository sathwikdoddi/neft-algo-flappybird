import pygame
import random

COLOR_WHITE = (255, 255, 255)

class Ground:
    height_from_top = 550
    COLOR_WHITE = (255, 255, 255)

    def __init__(self, window_width):
        self.y = self.height_from_top
        self.ground = pygame.Rect(0, self.y, window_width, 5)

    def draw_ground(self, window):
        pygame.draw.rect(window, COLOR_WHITE, self.ground)

class Obstacles:
    width = 12
    gap_height = 80

    def __init__(self, window_width):
        self.passed = False
        self.off_screen = False

        self.x = window_width
        self.bottom_height = random.randint(10, 350)
        self.top_height  = Ground.height_from_top - self.bottom_height - self.gap_height

        self.bottom_component = pygame.Rect(self.x, Ground.height_from_top - self.bottom_height, self.width, self.bottom_height)
        self.top_component = pygame.Rect(self.x, 0, self.width, self.top_height)
    
    def draw_obstacles(self, window):
        self.bottom_component = pygame.Rect(self.x, Ground.height_from_top - self.bottom_height, self.width, self.bottom_height)
        self.top_component = pygame.Rect(self.x, 0, self.width, self.top_height)

        pygame.draw.rect(window, COLOR_WHITE, self.top_component)
        pygame.draw.rect(window, COLOR_WHITE, self.bottom_component)
    
    def move(self):
        self.x  -= 1
        if (self.x + Obstacles.width <= 50):
            self.passed = True
        if (self.x <= -self.width):
            self.off_screen = True
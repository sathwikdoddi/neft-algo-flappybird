import pygame
from sys import exit
import setup
import elements
import population

BLACK_COLOR = (0, 0 ,0)

pygame.init()
clock = pygame.time.Clock()
population = population.Population(10)

def generate_obstacle():
    setup.obstacles.append(elements.Obstacles(setup.window_width))

def main():
    ticks_until_obstacle_spawn = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        setup.window.fill(BLACK_COLOR)
        setup.ground.draw_ground(setup.window)
        
        if ticks_until_obstacle_spawn <= 0:
            generate_obstacle()
            ticks_until_obstacle_spawn = 180
        ticks_until_obstacle_spawn -= 1

        for obstacle in setup.obstacles:
            obstacle.draw_obstacles(setup.window)
            obstacle.move()
            if obstacle.off_screen:
                setup.obstacles.remove(obstacle)
        
        if not population.extinct():
            population.update_birds()

        clock.tick(60)
        pygame.display.flip()
        pygame.display.set_caption("NEFT Flappy Bird")

main()
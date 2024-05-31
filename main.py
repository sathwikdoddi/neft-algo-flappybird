import pygame
from sys import exit
import config
import components
import population

COLOR_BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def main():
    pipes_spawn_time = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        config.window.fill(COLOR_BLACK)
        config.ground.draw(config.window)

        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)

        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            population.natural_selection()

        clock.tick(60)
        pygame.display.flip()
        pygame.display.set_caption("NEFT Flappy Bird")

main()
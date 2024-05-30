import pygame
import random
import setup
import brain

class Bird:
    def __init__(self):
        self.x = 50
        self.y = 265
        self.bird = pygame.Rect(self.x, self.y, 20, 20)
        self.color = (random.randint(150, 255), random.randint(100, 255), random.randint(100, 255))

        self.velocity = 0
        self.flap = False
        self.alive = True

        self.network_decision = None
        self.data = [0.5, 1, 0.5]
        self.inputs = 3
        self.brain = brain.Brain(self.inputs)
        self.brain.generate_network()
    
    def draw_player(self, window):
        pygame.draw.rect(window, self.color, self.bird)
    
    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.bird, ground)
    def sky_collision(self):
        return bool(self.bird.y < 30)
    def pipe_collision(self):
        for obstacle in setup.obstacles:
            return pygame.Rect.colliderect(self.bird, obstacle.top_component) or pygame.Rect.colliderect(self.bird, obstacle.bottom_component)
    
    def update(self, ground):
        velocity_max = 4.5
        accel = 0.22
        if not (self.ground_collision(ground) or self.pipe_collision()):
            self.velocity += accel
            self.bird.y += self.velocity
            if self.velocity > velocity_max:
                self.velocity = velocity_max
        else:
            self.alive = False
    
    def bird_flapping(self):
        if not self.flap and not self.sky_collision():
            self.flap = True
            self.velocity = -4.5
        if self.velocity >= 3:
            self.flap = False
    
    def random_flapping(self):
        self.network_decision = self.brain.feed_inputs(self.data)
        if self.network_decision > 0.73:
            self.bird_flapping()

    def get_data(self):
        if setup.obstacles:
            self.data[0] = max(0, self.bird.center[1] - self.closest_pipe().top_component.bottom) / 400
            pygame.draw.line(setup.window, self.color, self.bird.center, (self.bird.center[0], self.closest_pipe().top_component.bottom))

            self.data[1] = max(0, self.closest_pipe().x - self.bird.center[0]) / 400
            pygame.draw.line(setup.window, self.color, self.bird.center, (self.closest_pipe().x, self.bird.center[1]))

            self.data[2] = max(0, self.closest_pipe().bottom_component.top - self.bird.center[1]) / 400
            pygame.draw.line(setup.window, self.color, self.bird.center, (self.bird.center[0], self.closest_pipe().bottom_component.top))
            
    @staticmethod
    def closest_pipe():
        for obstacle in setup.obstacles:
            if not obstacle.passed:
                return obstacle
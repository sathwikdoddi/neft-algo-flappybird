import setup
import bird

class Population:
    def __init__(self, size):
        self.birds = []
        self.size = size
        for i in range(size):
            self.birds.append(bird.Bird())
    
    def update_birds(self):
        for bird in self.birds:
            if bird.alive:
                bird.get_data()
                bird.random_flapping()
                bird.draw_player(setup.window)
                bird.update(setup.ground.ground)
    
    def extinct(self):
        ret = True
        for bird in self.birds:
            if bird.alive:
                ret = False
        return ret
from random import choice

class RandomWalk():
    """ A class that randomly generate data"""
    
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        """Genereate walking path"""

        while len(self.x) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Avoid going nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # get Next position based on last position
            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step

            self.x.append(next_x)
            self.y.append(next_y)
    
    def get_step(self):
        """get walking step"""
        direction = choice([1, -1])
        distance = choice([i for i in range(5)])
        step = direction * distance

        return step

from random import choice

class RandomWalks:
    def __init__(self, num_points = 5000):
        self.sum_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]
        
    
    def fill_walk(self):
        while len(self.x_values) < self.sum_points:
            
            x_step = self.get_step()
            y_step = self.get_step()
            
            if x_step == y_step:
                continue
            
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)           
            
    def get_step(self):
        dir = choice([1,-1])
        dist = choice(range(20))

        return dir * dist
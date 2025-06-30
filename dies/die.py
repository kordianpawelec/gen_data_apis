

from random import randint

class Die:
    def __init__(self, tosses, dies, number_of_size):
        self.tosses = tosses
        self.outcomes = []
        self.dies = dies
        self.number_of_size = number_of_size
        
        
    def toss(self):
        for _ in range(self.tosses):
            _sum = 0
            for j in range(self.dies):
                _sum += randint(1, self.number_of_size)
            self.outcomes.append(_sum)
        
        
import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for attribute, value in kwargs.items():
            setattr(self,attribute, value)
            for v in range(0,value):
                self.contents.append(attribute)

    def draw(self, balls):
        draw_list = list()
        num_balls = min(balls, len(self.contents))
        for i in range(num_balls):
            idx = random.randrange(len(self.contents))
            draw_list.append(self.contents[idx])
            self.contents.pop(idx)
        return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    
    for _ in range(num_experiments):
        ext_hat = copy.deepcopy(hat)
        draw = ext_hat.draw(num_balls_drawn) 
        count_colour = 0   
        
        for i in expected_balls.keys():
            if draw.count(i)>= expected_balls[i]:
                count_colour +=1 
        
        if count_colour == len(expected_balls):
            count+=1
    probability = count/num_experiments
    
    return probability


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print("Probability:",probability)
import copy
import random

class Hat: # Create the fake 'hat' the balls are in

    def __init__(self, **kwargs): # Allows any number of inputs 
        self.contents=[]

        for key, value in kwargs.items(): 
            setattr(self,key,value)

        for key,value in kwargs.items(): # Adds how ever many items inputted as a list
            iterator=0
            while iterator < value:
                iterator+=1
                self.contents.append(key)

        self.copy_content=list(self.contents)
        self.full_match=0


    def draw(self,balls_to_draw): # Draws balls from the hat and removes them from the total once drawn

        if balls_to_draw >= len(self.contents): # Checks to see if the input is greater than the number of balls in the hat
            return self.contents
        
        drawn_list=[]
        for x in range(balls_to_draw): # Randomly picks balls out of how ever many are currently in the hat
            random_index=random.randrange(len(self.copy_content))
            random_ball=self.copy_content[random_index]
            del self.copy_content[random_index] # Removes the ball from the hat
            drawn_list.append(random_ball) # Adds the drawn ball to the output
        
        return drawn_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments): # Runs the number of experiments to find the probability of pulling whats expected
    
    for y in range(num_experiments): # Runs for x amount of experiments
        hat.copy_content = copy.deepcopy(hat.contents) # Creates a deepcopy otherwise the data in contents gets deleted when drawing balls from the hat
        # Reset the Dictionary and matching pairs each experiment
        ball_dict=dict()
        matching_pairs=0
        for x in hat.draw(num_balls_drawn): # Adds how ever many of each ball is drawn
            if x in ball_dict:
                ball_dict[x]+=1
            else:
                ball_dict[x]=1

        for key,value in ball_dict.items(): # Checks to see if the matching balls are pulled
            if key in expected_balls and value >= expected_balls[key]:
                matching_pairs+=1
                if matching_pairs == len(expected_balls): # Confirms a full match if the matching pairs is the length of how ever many expected balls were
                    hat.full_match+=1

    probability= hat.full_match/num_experiments # Divides how ever many full matches there were against how many experiments
    return probability 
            


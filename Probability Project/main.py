import hat_class

# This project finds the probability of pulling inputed balls from a hat

hat_class.random.seed(95)
hat = hat_class.Hat(black=6,red=4,green=3)
print(hat.draw(5))
probability = hat_class.experiment(hat=hat,expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiments=2000)
print("Probability:", probability)
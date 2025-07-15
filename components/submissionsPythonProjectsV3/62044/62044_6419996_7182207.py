while True:
    import random
    import math
    import matplotlib.pyplot as plt
    inside = 0
   
    #Values that are less than 1000 technically do work, but due to how little amount of dots that would be, its hard to actually see it on the graph, which is why I ask the user to imput more than 1000.
    N = int(input('How many dots would you like to use to help estimate pi? Make sure the value is greater than 1000 and make sure there arent any decimals. To exit type 0: '))
    #The empty lists are made to hold the its corresponding points, these are useful for when we actually start plotting the graph itself
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
   
    if N >= 1000:
        for _ in range(N): #I create a look here to start imputing the points in the graph as long as its in the range of the input
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            d = math.sqrt(x**2 + y**2)

            if d <= 1: #We start assigning the numbers to their corrisponding positions based on the value of d
                inside += 1
                x_inside.append(x)
                y_inside.append(y)
            else:
                x_outside.append(x)
                y_outside.append(y)
        cal_pi= 4 * inside/N #This is where we get the estimated value based on how many dots ended up being inside the circle 
       
       
        def plot_points(x_inside, y_inside, x_outside, y_outside): #This functionis specifically for all the features of the graph. More importantly it is where we begin to plot the points onto a graph.
            plt.figure(figsize=(8, 8))
            plt.scatter(x_inside, y_inside, color='green', s=1, label="Inside circle")
            plt.scatter(x_outside, y_outside, color='red', s=1, label="Outside circle")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"Estimation of Pi using {N} samples, Calculated Pi: {cal_pi}")
            plt.legend()
            plt.gca().set_aspect('equal', adjustable='box')
            plt.show()
        plot_points(x_inside, y_inside, x_outside, y_outside) #after all the modifications, this is the function we end up with and the one thats shown when a value is calculated.
   
    #The following  elif statements are to make sure that the program doesnt close in case they input a value that is not valid
    elif N in range(1,1000):
        print('The value you chose is not valid')

    elif N <=-1:
        print('The value you chose is not valid')
    #this allows the user to close the program whenever they please
    elif N == 0:
        print('Exiting...')
        break

   






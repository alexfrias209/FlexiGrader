import sympy as sp 
import numpy as np                                                  # Importing revelant functions and shorten their calls
import matplotlib.pyplot as plt

                                                              
                                           
print("\nProject Description:")
print("This project demonstrates the Newton's method in Python.")

                                                                    # File Paths
derivative_file = "derivative.txt"
plot_file = "plot.png"
roots_file = "roots.txt"

                                                                   # Plotting Function
def plot_expression(user_func):
    x = sp.symbols('x')
    try:
        expression = sp.sympify(user_func)
        f = sp.lambdify(x, expression, 'numpy')                    #using numpy and sympy change the input func into an expression 
                                                                   #matplotlib can use
        x_domain = (-10, 10)                                       #domain of the graph
        num_points = 100                                           #number of points in given domain
        x_vals = np.linspace(x_domain[0], x_domain[1], num_points) #mapping x values given an array and number of points
        y_vals = f(x_vals)                                         #find y values using the function and x values prev found
        roots = sp.solve(expression, x)                            #find roots using sympy function
        plt.plot(x_vals, y_vals, label=user_func)                  #plot func using matlabplot
        for root in roots:                                         #iterate the plotting of roots using scatter plot from matlabplot
            plt.scatter(root, 0, color='blue', marker='o', label=f'Root: x = {root}')
                                                                   
                                                                   #Plot labels and Legend
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Plot of Function')
        plt.legend()
        plt.grid()
        plt.savefig(plot_file)
        plt.show()
    except (sp.SympifyError, ValueError):
        print("Invalid function. Please enter a valid function in terms of 'x.")

                                                                # Newton's Method Function
def newtons_method(function, x0, tolerance):
    x = sp.symbols('x')                                         # vars intialization
    f = sp.sympify(function)
    f_prime = sp.diff(f, x)
    x_n = x0

    while True:
        x_n1 = x_n - f.subs(x, x_n) / f_prime.subs(x, x_n)
        if abs(x_n1 - x_n) < tolerance:
            print(f'the root is {x_n1}')
            with open(roots_file, "w") as file:
                file.write(f"The approximate root is: {x_n1}")
            return x_n1
        x_n = x_n1


def derivative_calc(function):
    x = sp.symbols('x')
    func = sp.sympify(function)
    func_prime = sp.diff(func, x)
    with open(derivative_file, "w") as file:
        file.write(f"The derivative for function {func} is {func_prime}")
    
    
                                                                # User's Choice
while True:
    print("\nChoose an option:")
    print("1. Calculate using Newton's method.")
    print("2. Calculate derivative of a function using sympy.")
    print("3. Find roots graphically.")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print("You chose to use Newton's method.")               # Calculate using Newton's method
        function = input("Enter the function (in terms of x) to apply Newton's method on: ")
        tolerance = float(input("Enter the tolerance level: "))  
        initial_guess = float(input("Enter the initial guess: "))                                                                                  
        root = newtons_method(function, initial_guess, tolerance)
        print(root)

    elif choice == '2':
        print("You chose to find a derivative.")
        function = input("Enter a function (in terms of x) to calculate its derivative")
        derivative_calc(function)


    elif choice == '3':
        user_function = input("Enter a function in terms of 'x':")
        plot_expression(user_function)


    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    
    
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/).")

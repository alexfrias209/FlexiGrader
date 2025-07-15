import matplotlib.pyplot as plt
import numpy as np

print('\nWelcome to the Calculator Application!')
print('Use this Calculator Application to perform Addition, Subtraction, Multiplication, Division, Expression Evaluation and/or Graphing.\n')
exit = False

def addition(List):
    if '-' in List:
        return('\nPlease choose appropriate method!')
    if '*' in List:
        return('\nPlease choose appropriate method!')
    if '/' in List:
        return('\nPlease choose appropriate method!')
    numbers = List.split('+')
    List1 = []
    for i in range(len(numbers)):
        List1.append(float(numbers[i]))
    ans = 0
    for i in range(len(List1)):
        ans = ans + List1[i]
    return ans

def subtraction(List):
    if '+' in List:
        return('\nPlease choose appropriate method!')
    if '*' in List:
        return('\nPlease choose appropriate method!')
    if '/' in List:
        return('\nPlease choose appropriate method!')
    numbers = List.split('-')
    List1 = []
    for j in range(len(numbers)):
        List1.append(float(numbers[j]))
    ans = 0
    for j in range(len(List1)):
        ans = -ans - List1[j]
    return ans

def multiply(List):
    if '-' in List:
        return('\nPlease choose appropriate method!')
    if '+' in List:
        return('\nPlease choose appropriate method!')
    if '/' in List:
        return('\nPlease choose appropriate method!')
    numbers = List.split('*')
    List1 = []
    for k in range(len(numbers)):
        List1.append(float(numbers[k]))
    ans = 1
    for k in range(len(List1)):
        ans = ans * List1[k]
    return ans

def divide(List):
    if '-' in List:
        return('\nPlease choose appropriate method!')
    if '*' in List:
        return('\nPlease choose appropriate method!')
    if '+' in List:
        return('\nPlease choose appropriate method!')
    numbers = List.split('/')
    List1 = []
    for l in range(len(numbers)):
        List1.append(float(numbers[l]))
    ans = List1[0]
    for l in range(len(List1)-1):
        if (List1[l+1] == 0):
            return('\nDivide by 0 error.')
        ans = ans/List1[l+1]
    return ans

saved_list = []   
while (exit != True):
    print('\nChoose your desired operation: ')
    print('Enter 1 for Addition')
    print('Enter 2 for Subtraction')
    print('Enter 3 for Multiplication')
    print('Enter 4 for Division')
    print('Enter 5 for Expression')
    print('Enter 6 for Latest Three Performed Calculations')
    print('Enter 7 for Graphing Function')
    print('Enter "s" to Save Calculations')
    print('Enter 8 to exit the program')

    userInput = input('You chose: ')
    value = ""
    ans = ""
    if(userInput == '6'):
        with open('59974_6375250_4037698.txt','r') as file:
            file_contents = file.readlines()
            contents = ['','','']
            contents = [line.strip() for line in file_contents]

        if(len(contents) == 1):
            print(contents[-1])
        elif(len(contents) == 2):
            print(contents[-2])
            print(contents[-1])
        elif(len(contents) >= 3):
            print(contents[-3])
            print(contents[-2])
            print(contents[-1])
        
    if(userInput == '8'):
        print('Thank you for using the calculator!')
        exit = True
        break
    elif(userInput == '1'):
        print('You chose: Addition')
        value = input('Enter addition expression: ')
        ans = addition(value)
        print(addition(value))
        saved_list.append(value + ' = ' + str(ans) + '\n')
    elif(userInput == '2'):
        print('You chose: Subtraction')
        value = input('Enter subtraction expression: ')
        ans = subtraction(value)
        print(subtraction(value))
        saved_list.append(value + ' = ' + str(ans) + '\n')
    elif(userInput == '3'):
        print('You chose: Multiplication')
        value = input('Enter multiplication expression: ')
        ans = multiply(value)
        print(multiply(value))
        saved_list.append(value + ' = ' + str(ans) + '\n')
    elif(userInput == '4'):
        print('You chose: Division')
        value = input('Enter division expression: ')
        ans = divide(value)
        print(divide(value))
        saved_list.append(value + ' = ' + str(ans) + '\n')
    elif(userInput == '5'):
        print('You chose: Expression')
        value = input('Enter mathematical expression: ')
        ans = eval(value)
        print(eval(value))
        saved_list.append(value + ' = ' + str(ans) + '\n')

    elif(userInput == 's'):
        with open('59974_6375250_4037698.txt', 'a') as f:
            for item in saved_list[-3:]:
                f.write(item)
                
    elif(userInput == '7'):
        print('You chose: Graph Function')
        alg_expr = input('Enter an Algebraic Expression (In terms of x): ')
        value = alg_expr
        x_range = input('Enter the start and end x values (Separated by comma): ')
        accuracy = input('Accuracy (L (Low), M (Medium), H (High): ')
        num_pts = 25
        if (accuracy == 'L'):
            num_pts = 10
        elif (accuracy == 'M'):
            num_pts = 50
        elif (accuracy == 'H'):
            num_pts = 100
        split_x = [float(v.strip()) for v in x_range.split(',')]
        domain = np.linspace(split_x[0], split_x[1], num=num_pts)
        
        y_range = input('Enter the start and end y values (separated by comma): ')
        split_y = [float(v.strip()) for v in y_range.split(',')]

        y_values = []

        for x in domain:
            spec_expr = alg_expr.replace('x', str(float(x)))
            spec_expr = spec_expr.replace('e', str(round(np.e, 3))).replace('pi', str(round(np.pi, 3)))
            f_x = eval(spec_expr)
            y_values.append(f_x)
        print('View your graph!')

        plt.plot(domain, y_values, 'r--')
        plt.axis((split_x[0], split_x[1], split_y[0], split_y[1]))
        plt.show()
    if len(saved_list) > 3:
        saved_list.pop(0)
f = open('59974_6375250_4037698.txt','a')
f.writelines(saved_list[-3:])
print(contents)
f.close()

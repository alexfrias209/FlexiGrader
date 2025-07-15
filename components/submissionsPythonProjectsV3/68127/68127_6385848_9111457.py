import math
history = []
last_result = None
def get_number(prompt):
    if last_result is None:
        return float(input(prompt))
    else:
        choice = input('1. Use the last result as the first number (L)\n2. Enter a new number (N)\nEnter your choice (L/N): ')
        if choice in ['L', 'l']:
            return last_result
        elif choice in ['N', 'n']:
            return float(input(prompt))
        else:
            print('Invalid choice, so using the previous result.')
            return last_result
            
def add():
    num1 = get_number('Enter the first number: ')
    num2 = float(input('Enter the second number: '))
    result = num1 + num2
    history.append(result)
    return result
def subtract():
    num1 = get_number('Enter the first number: ')
    num2 = float(input('Enter the second number: '))
    result = num1 - num2
    history.append(result)
    return result
def multiply():
    num1 = get_number('Enter the first number: ')
    num2 = float(input('Enter the second number: '))
    result = num1 * num2
    history.append(result)
    return result
def divide():
    num1 = get_number('Enter the numerator: ')
    num2 = float(input('Enter the denominator: '))
    if num2 == 0:
        print('Error, denominator cannot be zero!!!')
        return None
    result = num1 / num2
    history.append(result)
    return result
def square_root():
    num = get_number('Enter the number: ')
    if num < 0:
        print('Error,cannot calculate square root with a negative number!!!')
        return None
    result = math.sqrt(num)
    history.append(result)
    return result
def sin():
    angle = get_number('Enter the angle in degrees: ')
    result = math.sin(math.radians(angle))
    history.append(result)
    return result
def cos():
    angle = get_number('Enter the angle in degrees: ')
    result = math.cos(math.radians(angle))
    history.append(result)
    return result
def tan():
    angle = get_number('Enter the angle in degrees: ')
    result = math.tan(math.radians(angle))
    history.append(result)
    return result
def view_history():
    print('The most recent three calculation results:')
    for idx, item in enumerate(history[-3:], start=1):
        print(f'{idx}. {item}')
def save_history():
    filename = input('Enter the filename to save the results,you can include the file format: ')
    with open(filename, 'w') as file:
        for item in history:
            file.write(str(item) + '\n')
    print(f'Results are saved to {filename}')
    
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
    '5': square_root,
    '6': sin,
    '7': cos,
    '8': tan,
    '9': view_history,
    '10': save_history
}

while True:
    print('Choose your calculating method:')
    for key, value in operations.items():
        print(f'{key}. {value.__name__}')
    print('11. exit')
    choice = input('Enter your option (1/2/3/4/5/6/7/8/9/10/11): ')
    if choice == '11':
        break
    elif choice in operations:
        operation = operations[choice]
        result = operation()
        if result is not None:
            last_result = result
            print('Result: ', result)
    else:
        print('Invalid, please re-enter!!')

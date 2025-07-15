
MyDic = {}
MyList = []
MyCapacitors = []
MyInductors = []
temp = 0
temp1 = 0
#Making a function for parallel/series calculations involving 1/x = 1/x1 + 1/x2...
def newfunction(x):
    temp2 = 0
    for i in x:
        temp2 += 1/i
    temp2 = 1/temp2
    return temp2
query = input('Option 1: Create a circuit with resistors, capacitors, and inductors to find total amounts of resistance, capacitance, and inductance throughout the circuit.\nOption 2: Define values to graph the voltage and current of an alternating circuit.\nUse "Option 1" or "Option 2" to select.\n')
#Originally I was going to let you make a graph based on this option, but RLC circuits are apparently really complicated when it comes to creating a graph of voltage and before I started this project I did not even know what inductance or capacitance were, so I decided to split my code into two options to maintain the loops I do not really need for the second option.
if query == 'Option 1' or query == 'option 1' or query == '1':
    #How many times does the current split?
    Parallels = float(input('How many parallel branches are in this circuit? Enter 1 if it is a single-loop circuit.\n'))
    #Code for branches
    if Parallels > 1:
        #Resistors
        MyDic['ResistorsStart'] = float(input('How many resistors are there before the branches split?\n'))
        while temp < MyDic['ResistorsStart']:
            temp += 1
            MyDic['StartResistor{0}'.format(temp)] = float(input('What is the resistance of resistor {0} of the start in ohms?\n'.format(temp)))
            MyList.append(MyDic['StartResistor{0}'.format(temp)])
        if temp >=1:
            ResistanceStart = sum(MyList)
        else:
            ResistanceStart = 0
        temp = 0
        MyList.clear()
        #Capacitor
        MyDic['CapacitorStart'] = input('Is there a capacitor before the circuit splits? Yes or no?\n')
        if MyDic['CapacitorStart'] == 'Yes' or MyDic['CapacitorStart'] == 'yes':
            MyDic['StartCapacitor'] = float(input('What is the capacitance of this capacitor in microfarads?\n'))
            MyCapacitors.append(MyDic['StartCapacitor'])
        #Inductor
        MyDic['InductorStart'] = input('Is there a Inductor before the circuit splits? Yes or no?\n')
        if MyDic['InductorStart'] == 'Yes' or MyDic['InductorStart'] == 'yes':
            MyDic['StartInductor'] = float(input('What is the inductance of this inductor in millihenries?\n'))
            MyInductors.append(MyDic['StartInductor'])
        #Resistors in parallel branches
        while temp < Parallels:
            temp += 1
            MyDic['Resistors{0}'.format(temp)] = float(input('How many resistors are in branch {0}?\n'.format(temp)))
            while temp1 < MyDic['Resistors{0}'.format(temp)]:
                temp1 += 1
                MyDic['Parallel{0}Resistor{1}'.format(temp, temp1)] = float(input('What is the resistance of resistor {0} of this branch in ohms?\n'.format(temp1)))
                MyList.append(MyDic['Parallel{0}Resistor{1}'.format(temp, temp1)])
            temp1 = 0
        if not MyList:
            ResistanceBranches = 0
        else:
            ResistanceBranches = newfunction(MyList)
        MyList.clear()
        temp = 0
        #Capacitors in parallel branches
        while temp < Parallels:
            temp += 1
            MyDic['Capacitor{0}'.format(temp)] = input('Is there a capacitor in branch {0}? Yes or no?\n'.format(temp))
            if MyDic['Capacitor{0}'.format(temp)] == 'Yes' or MyDic['Capacitor{0}'.format(temp)] == 'yes':
                MyDic['Capacitor{0}'.format(temp)] = float(input('What is the capacitance of this capacitor in this branch in microfarads?\n'))
                MyList.append(MyDic['Capacitor{0}'.format(temp)])
        if len(MyList) != 0:
            CapacitanceBranches = sum(MyList)
            MyCapacitors.append(CapacitanceBranches)
            MyList.clear()
        temp = 0
        #Inductors in parallel branches
        while temp < Parallels:
            temp += 1
            MyDic['Inductor{0}'.format(temp)] = input('Is there an inductor in branch {0}? Yes or no?\n'.format(temp))
            if MyDic['Inductor{0}'.format(temp)] == 'Yes' or MyDic['Inductor{0}'.format(temp)] == 'yes':
                MyDic['Inductor{0}'.format(temp)] = float(input('What is the inductance of this inductor in this branch in millihenries?\n'))
                MyList.append(MyDic['Inductor{0}'.format(temp)])
        if len(MyList) != 0:
            InductanceBranches = newfunction(MyList)
            MyInductors.append(InductanceBranches)
            MyList.clear()
        temp = 0
        #Code for resistors after branches converge
        MyDic['ResistorsEnd'] = float(input('How many resistors are there after the branches converge?\n'))
        while temp < MyDic['ResistorsEnd']:
            temp += 1
            MyDic['EndResistor{0}'.format(temp)] = float(input('What is the resistance of resistor {0} of the end in ohms?\n'.format(temp)))
            MyList.append(MyDic['EndResistor{0}'.format(temp)])
        if temp >=1:
            ResistanceEnd = sum(MyList)
        else:
            ResistanceEnd = 0
        temp = 0
        MyList.clear()
        MyList.append(ResistanceStart)
        MyList.append(ResistanceBranches)
        MyList.append(ResistanceEnd)
        ResistanceTotal = sum(MyList)
        MyList.clear
        #Code for capacitors after branches converge
        MyDic['CapacitorEnd'] = input('Is there a capacitor after the branches converge? Yes or no?\n')
        if MyDic['CapacitorEnd'] == 'Yes' or MyDic['CapacitorEnd'] == 'yes':
            MyDic['EndCapacitor'] = float(input('What is the capacitance of this capacitor in microfarads?\n'))
            MyCapacitors.append(MyDic['EndCapacitor'])
        if len(MyCapacitors) != 0:
            CapacitanceTotal = newfunction(MyCapacitors)
        else:
            CapacitanceTotal = 0
        #Code for inductors after branches converge
        MyDic['InductorEnd'] = input('Is there an inductor after the branches converge? Yes or no?\n')
        if MyDic['InductorEnd'] == 'Yes' or MyDic['InductorEnd'] == 'yes':
            MyDic['EndInductor'] = float(input('What is the inductance of this inductor in millihenries?\n'))
            MyInductors.append(MyDic['EndInductor'])
        if len(MyInductors) != 0:
            InductanceTotal = sum(MyInductors)
        else:
            InductanceTotal = 0
    #Code for no branches
    elif Parallels == 1:
        #Resistors
        MyDic['Resistors'] = float(input('How many resistors are there?\n'))
        while temp < MyDic['Resistors']:
            temp += 1
            MyDic['Resistor{0}'.format(temp)] = float(input('What is the resistance of resistor {0} in ohms?\n'.format(temp)))
            MyList.append(MyDic['Resistor{0}'.format(temp)])
        temp = 0
        if len(MyList) != 0:
            ResistanceTotal = newfunction(MyList)
        else:
            ResistanceTotal = 0
        #Capacitors
        MyDic['Capacitor'] = input('Is there a capacitor? Yes or no?\n')
        if MyDic['Capacitor'] == 'yes' or MyDic['Capacitor'] == 'Yes':
            CapacitanceTotal = float(input('What is the capacitance of this capacitor in microfarads?\n'))
        else:
            CapacitanceTotal = 0
        #Inductors
        MyDic['Inductor'] = input('Is there an inductor? Yes or no?\n')
        if MyDic['Inductor'] == 'yes' or MyDic['Inductor'] == 'Yes':
            InductanceTotal = float(input('What is the inductance of this inductor in millihenries?\n'))
        else:
            InductanceTotal = 0
    #Code for failed input
    else:
        print('The entered amount is not applicable.')
    #print(MyDic)
    #print(MyList)
    #code outputs
    print('The total resistance of the circuit is ', end='')
    print("{:.2f}".format(ResistanceTotal), 'ohms.')
    print('The total capacitance of the circuit is ', end='')
    print("{:.2f}".format(CapacitanceTotal), 'microfarads.')
    print('The total inductance of the circuit is ', end='')
    print("{:.2f}".format(InductanceTotal), 'millihenries.')
#start of code for option 2
#after not being able to figure out how to convert an RLC circuit into a voltage graph, I decided the next best thing might be to let the user decide on the variables in an ac circuit to see how they affect the graph
elif query == 'Option 2' or query == 'option 2' or query == '2':
    #voltage(t) = Vamplitude * sin (2pi * frequency * time)
    #current(t) = Iamplitude * sin (2pi * frequency * time)
    vamp = float(input('Enter the amplitude of the voltage.\n'))
    iamp = float(input('Enter the amplitude of the current.\n'))
    f = float(input('Enter the frequency.\n'))
    pa = float(input('Enter the phase angle between 0 and 2pi that creates a phase difference between voltage and current.\n'))
    pltrng = float(input('Enter the amount of seconds to plot.\n'))
    # Import libraries
    import matplotlib.pyplot as plt
    import numpy as np
    #Plotting a graph of the current and voltage using numpy and matplotlib
    t = np.linspace(0, pltrng, 1000)
    V = vamp * np.sin((6.282 * f) * t)
    I = iamp * np.sin((6.282 * f) * t + pa)
    fig = plt.figure(figsize = (10, 7))
    plt.plot(t, V, label='Voltage')
    plt.plot(t, I, label='Current')
    #decorating the graph
    plt.title('Voltage and Current of an AC Power Source')
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Amplitude')
    plt.axhline(y=0, color='k')
    plt.grid(True, which='both')
    plt.legend()
    plt.show()
#code for failed input
else:
    print('Expected either Option 1 or Option 2.')
input('\nThe code is finished.\n')

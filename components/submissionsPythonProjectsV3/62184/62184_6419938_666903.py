from tabulate import tabulate
element_data = {
    'H': {'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008},
    'He': {'name': 'Helium', 'atomic_number': 2, 'atomic_mass': 4.0026},
    'Li': {'name': 'Lithium', 'atomic_number': 3, 'atomic_mass': 6.94},
    'Be': {'name': 'Beryllium', 'atomic_number': 4, 'atomic_mass': 9.0122},
    'B': {'name': 'Boron', 'atomic_number': 5, 'atomic_mass': 10.81},
    'C': {'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.01},
    'N': {'name': 'Nitrogen', 'atomic_number': 7, 'atomic_mass': 14.01},
    'O': {'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 16.00},
    'F': {'name': 'Fluorine', 'atomic_number': 9, 'atomic_mass': 19.00},
    'Ne': {'name': 'Neon', 'atomic_number': 10, 'atomic_mass': 20.18},
    'Na': {'name': 'Sodium', 'atomic_number': 11, 'atomic_mass': 22.99},
    'Mg': {'name': 'Magnesium', 'atomic_number': 12, 'atomic_mass': 24.31},
    'Al': {'name': 'Aluminum', 'atomic_number': 13, 'atomic_mass': 26.98},
    'Si': {'name': 'Silicon', 'atomic_number': 14, 'atomic_mass': 28.09},
    'P': {'name': 'Phosphorus', 'atomic_number': 15, 'atomic_mass': 30.97},
    'S': {'name': 'Sulfur', 'atomic_number': 16, 'atomic_mass': 32.07},
    'Cl': {'name': 'Chlorine', 'atomic_number': 17, 'atomic_mass': 35.45},
    'Ar': {'name': 'Argon', 'atomic_number': 18, 'atomic_mass': 39.95},
    'K': {'name': 'Potassium', 'atomic_number': 19, 'atomic_mass': 39.10},
    'Ca': {'name': 'Calcium', 'atomic_number': 20, 'atomic_mass': 40.08},
    'Sc': {'name': 'Scandium', 'atomic_number': 21, 'atomic_mass': 44.96},
    'Ti': {'name': 'Titanium', 'atomic_number': 22, 'atomic_mass': 47.87},
    'V': {'name': 'Vanadium', 'atomic_number': 23, 'atomic_mass': 50.94},
    'Cr': {'name': 'Chromium', 'atomic_number': 24, 'atomic_mass': 51.996},
    'Mn': {'name': 'Manganese', 'atomic_number': 25, 'atomic_mass': 54.94},
    'Fe': {'name': 'Iron', 'atomic_number': 26, 'atomic_mass': 55.85},
    'Co': {'name': 'Cobalt', 'atomic_number': 27, 'atomic_mass': 58.93},
    'Ni': {'name': 'Nickel', 'atomic_number': 28, 'atomic_mass': 58.69},
    'Cu': {'name': 'Copper', 'atomic_number': 29, 'atomic_mass': 63.55},
    'Zn': {'name': 'Zinc', 'atomic_number': 30, 'atomic_mass': 65.38},
    'Ga': {'name': 'Gallium', 'atomic_number': 31, 'atomic_mass': 69.72},
    'Ge': {'name': 'Germanium', 'atomic_number': 32, 'atomic_mass': 72.63},
    'As': {'name': 'Arsenic', 'atomic_number': 33, 'atomic_mass': 74.92},
    'Se': {'name': 'Selenium', 'atomic_number': 34, 'atomic_mass': 78.97},
    'Br': {'name': 'Bromine', 'atomic_number': 35, 'atomic_mass': 79.90},
    'Kr': {'name': 'Krypton', 'atomic_number': 36, 'atomic_mass': 83.80},
    'Rb': {'name': 'Rubidium', 'atomic_number': 37, 'atomic_mass': 85.47},
    'Sr': {'name': 'Strontium', 'atomic_number': 38, 'atomic_mass': 87.62},
    'Y': {'name': 'Yttrium', 'atomic_number': 39, 'atomic_mass': 88.91},
    'Zr': {'name': 'Zirconium', 'atomic_number': 40, 'atomic_mass': 91.22},
    'Nb': {'name': 'Niobium', 'atomic_number': 41, 'atomic_mass': 92.91},
    'Mo': {'name': 'Molybdenum', 'atomic_number': 42, 'atomic_mass': 95.94},
    'Tc': {'name': 'Technetium', 'atomic_number': 43, 'atomic_mass': 98},
    'Ru': {'name': 'Ruthenium', 'atomic_number': 44, 'atomic_mass': 101.1},
    'Rh': {'name': 'Rhodium', 'atomic_number': 45, 'atomic_mass': 102.9},
    'Pd': {'name': 'Palladium', 'atomic_number': 46, 'atomic_mass': 106.4},
    'Ag': {'name': 'Silver', 'atomic_number': 47, 'atomic_mass': 107.9},
    'Cd': {'name': 'Cadmium', 'atomic_number': 48, 'atomic_mass': 112.4},
    'In': {'name': 'Indium', 'atomic_number': 49, 'atomic_mass': 114.8},
    'Sn': {'name': 'Tin', 'atomic_number': 50, 'atomic_mass': 118.7},
    'Sb': {'name': 'Antimony', 'atomic_number': 51, 'atomic_mass': 121.8},
    'Te': {'name': 'Tellurium', 'atomic_number': 52, 'atomic_mass': 127.6},
    'I': {'name': 'Iodine', 'atomic_number': 53, 'atomic_mass': 126.9},
    'Xe': {'name': 'Xenon', 'atomic_number': 54, 'atomic_mass': 131.3},
    'Cs': {'name': 'Cesium', 'atomic_number': 55, 'atomic_mass': 132.9},
    'Ba': {'name': 'Barium', 'atomic_number': 56, 'atomic_mass': 137.3},
    'La': {'name': 'Lanthanum', 'atomic_number': 57, 'atomic_mass': 138.9},
    'Ce': {'name': 'Cerium', 'atomic_number': 58, 'atomic_mass': 140.1},
    'Pr': {'name': 'Praseodymium', 'atomic_number': 59, 'atomic_mass': 140.9},
    'Nd': {'name': 'Neodymium', 'atomic_number': 60, 'atomic_mass': 144.2},
    'Pm': {'name': 'Promethium', 'atomic_number': 61, 'atomic_mass': 145},
    'Sm': {'name': 'Samarium', 'atomic_number': 62, 'atomic_mass': 150.4},
    'Eu': {'name': 'Europium', 'atomic_number': 63, 'atomic_mass': 152},
    'Gd': {'name': 'Gadolinium', 'atomic_number': 64, 'atomic_mass': 157.3},
    'Tb': {'name': 'Terbium', 'atomic_number': 65, 'atomic_mass': 158.9},
    'Dy': {'name': 'Dysprosium', 'atomic_number': 66, 'atomic_mass': 162.5},
    'Ho': {'name': 'Holmium', 'atomic_number': 67, 'atomic_mass': 164.9},
    'Er': {'name': 'Erbium', 'atomic_number': 68, 'atomic_mass': 167.3},
    'Tm': {'name': 'Thulium', 'atomic_number': 69, 'atomic_mass': 168.9},
    'Yb': {'name': 'Ytterbium', 'atomic_number': 70, 'atomic_mass': 173.0},
    'Lu': {'name': 'Lutetium', 'atomic_number': 71, 'atomic_mass': 175.0},
    'Hf': {'name': 'Hafnium', 'atomic_number': 72, 'atomic_mass': 178.5},
    'Ta': {'name': 'Tantalum', 'atomic_number': 73, 'atomic_mass': 180.9},
    'W': {'name': 'Tungsten', 'atomic_number': 74, 'atomic_mass': 183.8},
    'Re': {'name': 'Rhenium', 'atomic_number': 75, 'atomic_mass': 186.2},
    'Os': {'name': 'Osmium', 'atomic_number': 76, 'atomic_mass': 190.2},
    'Ir': {'name': 'Iridium', 'atomic_number': 77, 'atomic_mass': 192.2},
    'Pt': {'name': 'Platinum', 'atomic_number': 78, 'atomic_mass': 195.1},
    'Au': {'name': 'Gold', 'atomic_number': 79, 'atomic_mass': 197.0},
    'Hg': {'name': 'Mercury', 'atomic_number': 80, 'atomic_mass': 200.6},
    'Tl': {'name': 'Thallium', 'atomic_number': 81, 'atomic_mass': 204.4},
    'Pb': {'name': 'Lead', 'atomic_number': 82, 'atomic_mass': 207.2},
    'Bi': {'name': 'Bismuth', 'atomic_number': 83, 'atomic_mass': 208.9},
    'Th': {'name': 'Thorium', 'atomic_number': 90, 'atomic_mass': 232.0},
    'Pa': {'name': 'Protactinium', 'atomic_number': 91, 'atomic_mass': 231.0},
    'U': {'name': 'Uranium', 'atomic_number': 92, 'atomic_mass': 238.0},
    'Np': {'name': 'Neptunium', 'atomic_number': 93, 'atomic_mass': 237.0},
    'Pu': {'name': 'Plutonium', 'atomic_number': 94, 'atomic_mass': 244.0},
    'Am': {'name': 'Americium', 'atomic_number': 95, 'atomic_mass': 243.0},
    'Cm': {'name': 'Curium', 'atomic_number': 96, 'atomic_mass': 247.0},
    'Bk': {'name': 'Berkelium', 'atomic_number': 97, 'atomic_mass': 247.0},
    'Cf': {'name': 'Californium', 'atomic_number': 98, 'atomic_mass': 251.0},
    'Es': {'name': 'Einsteinium', 'atomic_number': 99, 'atomic_mass': 252.0},
    'Fm': {'name': 'Fermium', 'atomic_number': 100, 'atomic_mass': 257.0},
    'Md': {'name': 'Mendelevium', 'atomic_number': 101, 'atomic_mass': 258.0},
    'No': {'name': 'Nobelium', 'atomic_number': 102, 'atomic_mass': 259.0},
    'Lr': {'name': 'Lawrencium', 'atomic_number': 103, 'atomic_mass': 262.0},
}

print("Welcome to C-me or chemistry made easy.")
print("I")
print("The goal of my code is to make a smart periodic table.")

while True:
    yuy = input('Please input the symbol of the desired element: ')
    if yuy in element_data:
        element_info = element_data[yuy]
        print(f"You have chosen {yuy} or {element_info['name']}.")
        break
    else:
        print("Element not found. Please enter a valid element symbol.")

print("The next steps are to choose what to do with the element.")
while True:
    options = int(input("Type 1 to enter a new element or Type 2 to pull up elements atomic number and atomic mass or 3 to pull up a table or type 4 to quit (1, 2, 3, or 4): "))
    if options == 1:
        yuy = input("Enter an element symbol (or 'quit' to exit): ").capitalize()
        if yuy in element_data:
            element_info = element_data[yuy]
            print(f"You have chosen {yuy} or {element_info['name']}.")
        elif yuy == "Quit":
            break
        else:
            print(f"Element symbol '{yuy}' not found in the dictionary.")
    elif options == 2:
        if element_info is not None:
            print(f"The atomic number of {yuy} is {element_info['atomic_number']}.")
            print(f"The atomic mass of {yuy} is {element_info['atomic_mass']} amu.")
            break
    elif options == 3:
        tut = input("pick element to put on the table ").capitalize()
        eleminfo = element_data[tut]
        mydata = [[{element_info['name']}, {element_info['atomic_number']}, {element_info['atomic_mass']}],
        [{eleminfo['name']}, {eleminfo['atomic_number']}, {eleminfo['atomic_mass']}]]
        head = ['Name', 'A-Number', 'A-Mass']
        print(tabulate(mydata, headers=head, tablefmt="grid"))
    elif options == 4:
        break
        
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")

print('Thank you come back any time!')
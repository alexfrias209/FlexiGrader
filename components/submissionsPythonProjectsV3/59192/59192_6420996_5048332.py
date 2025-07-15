print('Welcome to my project about Material Life Cycle Analysis')
print()
print()
print('Explore the environmental impact and carbon footprint of materials in production.')
print()
print('Pick a material, variation of that material, and then be informed on its carbon footprint.')
print()
print('Please choose a material to explore:')
print('1. Plastic')
print('2. Metals')
print('3. Composites')

def main():
        decision = int(input('Enter your choice (1/2/3):'))

        if decision == 1:
            print('You chose to explore plastics. What kind of plastic would you like to explore?')

            print('1. Polycarbonate')

            print('2. Acrylic')

            print('3. Nylon')

            plastic = int(input('Enter your choice of plastic, (1/2/3):'))

            if plastic == 1:
                print('You chose to explore the plastic type: Polycarbonate')
                print('The carbon footprint of polycarbonate plastic can vary based on production methods and sources of raw materials.')
                print('Generally, plastic production has a significant carbon footprint due to the energy-intensive processes involved.')
        

            elif plastic == 2:
                print('You chose to explore the plastic type: Acrylic')
                print('Acrylics also have a carbon footprint associated with their production.')
                print('Again, the exact value can depend on manufacturing practices and location.')


            elif plastic == 3:
                print('You chose to explore the plastic type: Nylon')
                print('Nylon production is energy-intensive, contributing to its carbon footprint.')
                print('The specific carbon footprint can vary based on the type of nylon and the production process.')

            else:
                print('You have not entered the correct number signifying the element you want to explore.')
                Repeat = input('Would you like to run again? (yes or no)').lower()

                if Repeat == 'yes':
                    main()

                else:
                    print('Goodbye, have a beautiful day! :)')
                    exit()

        elif decision == 2:
            print('You chose to explore metals. What kind of metal would you like to explore?')

            print('1. Lead')

            print('2. Tin')

            print ('3. Aluminum')

            metal = int(input('Enter your choice of metal, (1/2/3):'))

            if metal == 1:
                print('You chose to explore the metal type: Lead')
                print('Lead is a heavy metal with known environmental and health concerns.')
                print('The carbon footprint associated with lead primarily comes from mining, extraction, and processing.')

            elif metal == 2:
                print('You chose to explore the metal type: Tin')
                print('Tin production involves mining and smelting, both of which contribute to its carbon footprint.')
                print('The carbon emissions depend on the source of tin and the extraction methods used.')

            elif metal == 3:
                print('You chose to explore the metal type: Aluminum')
                print(' Aluminum production is known to have a high carbon footprint due to the energy-intensive nature of the electrolytic reduction process used to extract aluminum from bauxite ore.')

            else:
                print('You have not entered the correct number signifying the element you want to explore.')
                Repeat = input('Would you like to run again? (yes or no)').lower()
                if Repeat == 'yes':
                    main()

                else:
                    print('Goodbye, have a beautiful day! :)')
                    exit()

        elif decision == 3:
            print('You chose to explore composites. What kind of composites would you like to explore?')

            print('1. Wood-Plastic composite')
            print('2. Carbon Fiber')
            print('3. Epoxy')

            composite = int(input('Enter your choice of composite, (1/2/3):'))

            if composite == 1:
                print('You chose to explore the composite type: Wood-Plastic')
                print('Wood-plastic composites combine wood fibers with plastic, and the carbon footprint depends on the ratio of wood to plastic and the energy used in the manufacturing process.')

            elif composite == 2:
                print('You chose to explore the composite type: Carbon Fiber')
                print('Carbon fiber production involves the oxidation and carbonization of a precursor material.')
                print("It's energy-intensive and typically has a substantial carbon footprint.")
        

            elif composite == 3:
                print('You chose to explore the composite type: Epoxy')
                print('Epoxy resin production involves the use of petroleum-based feedstocks and chemical processes, contributing to its carbon footprint.')
            else:
                print('You have not entered the correct number signifying the element you want to explore.')
                Repeat = input('Would you like to run again? (yes or no)').lower()
                if Repeat == 'yes':
                    main()

                else:
                    print('Goodbye, have a beautiful day! :)')
                    exit()

        else:
            print('You have not entered the correct number signifying the element you want to explore.')
            Repeat = input('Would you like to run again? (yes or no)').lower()
            if Repeat == 'yes':
                main()

            else:
                print('Goodbye, have a beautiful day! :)')
                exit()
main()
    

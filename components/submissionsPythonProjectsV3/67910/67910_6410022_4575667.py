import matplotlib.pyplot as plt
#List     =[["Material", spring constant, original Length(feet), Second Length(feet), area(inches) ],[etc...]]
materials = [['GOLD',float(0.92),int(5), int(10),int(15)],["ALUMINUM", float(0.81),int(5), int(10),int(15)],["TITANIUM", float(1.45),int(5), int(10),int(15)],["PLATINUM", float(2.06), int(5), int(10), int(15)]]
ans = True
while ans:
    print (""""
    1. Select Your own values for stress analysis on materials.
    2. Analyze stress on materials from a list
    3. EXIT SAM 
    """)
    ans=input("Welcome to Stress Analysis on Materials (SAM). What would you like to alanyze?")
    if ans=="1":
      user_mat = input("What material will be tested?")
      k = float(input('Enter a value for the Spring Constant of the material: '))
      length_1 = float(input('Enter a value for the original length of the material: '))
      length_2 = float(input('Enter a value for the second length of the material: '))
      area = float(input('Enter a value for the area of the material: '))
      X = length_1 - length_2
      F = -1 * k * X  # measured in newtons
      Hookes_law = F
      tensile_stress = F / area
      tensile_strain = X / length_1  # stretch
      compressive_stress = F / area
      compressive_strain = -1 * X / length_1
      shear_stress = F / area
      shear_strain = X / length_1
      G = shear_stress / shear_strain  # G modulus
      Young_modulus = compressive_stress / compressive_strain
      txt_output = print(f"""
      The Force value of {user_mat} is {Hookes_law}.
      The tensile strain of {user_mat} is {tensile_strain}.
      The shear strain of {user_mat} is {shear_strain}.
      The shear modulus of {user_mat} is {G}.
      """)
      x = range(-10, 20)
      force_values = [-k * val for val in x]
      plt.plot(x, force_values, label = "Hookes Law", linestyle = '--', color = 'blue')
      plt.xlabel('Change in length(x)')
      plt.ylabel('Force (F)')
      plt.title('Hookes law')
      plt.legend()
      plt.grid(True)
      plt.show()
      f = open('67910_6410023_4747754.txt', 'w')
      f.write(f"""
              The Force value of {user_mat} is {Hookes_law}.
              The tensile strain of {user_mat} is {tensile_strain}.
              print(f'The shear strain of {user_mat} is {shear_strain}.
              print(f'the shear modulus of {user_mat} is {G}.
              """)
      f.close()
      f = open("67910_6410023_4747754.txt", "r")
      print(f.read())
      print('The file has been updated. Thank you for choosing SAM')
    elif ans == "2":
      print("""
                   Material | Spring Constant
                       GOLD : 0.92
                   ALUMINUM : 0.81
                   TITANIUM : 1.45
                   PLATINUM : 2.06
        All values listed have unique spring constants.
        ALl values listed have an original length of 5 feet
        All values listed have a difference of 5 feet of length
        ALl values listed have an area of 15 inches squared
        
        """)
      user_option = input('Please choose one material as listed above(CASE SENSITIVE): ')
      chosen_mat = None
      for material in materials:
        if material[0] == user_option:
          chosen_mat = material
          break
      if chosen_mat:
        user_mat, k, length_1, length_2, area = chosen_mat
        X = length_1 - length_2
        F = -1 * k * X  # measured in newtons
        Hookes_law = F
        tensile_stress = F / area
        tensile_strain = X / length_1  # stretch
        compressive_stress = F / area
        compressive_strain = -1 * X / length_1
        shear_stress = F / area
        shear_strain = X / length_1
        G = shear_stress / shear_strain  # G modulus
        Young_modulus = compressive_stress / compressive_strain
        print(f"""
        The Force value of {user_mat} is {Hookes_law}.
        The tensile strain of {user_mat} is {tensile_strain}.
        print(f'The shear strain of {user_mat} is {shear_strain}.
        print(f'the shear modulus of {user_mat} is {G}.
        """)
        x = range(-10, 20)
        force_values = [-k * val for val in x]
        plt.plot(x, force_values, label="Hookes Law", linestyle='--', color='blue')
        plt.xlabel('Change in length(x)')
        plt.ylabel('Force (F)')
        plt.title('Hookes law')
        plt.legend()
        plt.grid(True)
        plt.show()
        f = open('67910_6410024_3666964.txt', 'w')
        f.write(f"""
        The Force value of {user_mat} is {Hookes_law}.
        The tensile strain of {user_mat} is {tensile_strain}.
        print(f'The shear strain of {user_mat} is {shear_strain}.
        print(f'the shear modulus of {user_mat} is {G}.
        """)
        f.close()
        f = open("67910_6410024_3666964.txt", "r")
        print(f.read())
        print('The file has been updated. Thank you for choosing SAM')
      else:
        print(f'{user_option} is not a valid choice. Please check for spelling mistakes or refer to the list above.')
    elif ans=="3":
      print("\n Thank you for choosing Project SAM.")
      break
    elif ans !="":
      print(f"\n {ans} is not a valid choice. Please enter a value from above.")


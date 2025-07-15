from Functions import * #Import funtoins from another file

import matplotlib.pyplot as plt #Import matplotlib to be able to create plots for the data
import numpy as np

#Functions Trail
#List of nesscary equations for Turbine Project can be found below



print("This is a program to help you determine the aircraft and flight parameters of your RC model aircraft.")

#List of avalaible turbines in the catalog
turbine_list = ["KingTech K-30G4+", "KingTech K-45G4+", "KingTech K-55G4+", "KingTech K-65G4+",
                "KingTech K-70G4+", "KingTech K-85G4+", "KingTech K-86G4+", "KingTech K-102G4+",
                "KingTech K-130G4+", "KingTech K-142G4+", "KingTech K-160G4+", "KingTech K-180G4+",
                "KingTech K-210G4+", "KingTech K-235G4+", "KingTech K-260G4+", "KingTech K-320G4+",
                "KingTech K-450G4+"]
for a in turbine_list:
    print(a)
    
##Asking for the turbine that the user would like to use in their 
turbine = input("What turbine are you using?(please look at the catalog)")

##The following are a series of dictionaries containing the values from a really online catalog of turbine for purchase
##They will be used to look up the values attached to the turbine name and then execute a series of functions (equations) to extract new values to be displayed for the user
##along with the creatation of lists to create trade study bar graphs from the data to better visulaize the data

turbine_dic_fuel = {"KingTech K-30G4+": 120, "KingTech K-45G4+": 150,
                    "KingTech K-55G4+": 200, "KingTech K-65G4+": 240,
                    "KingTech K-70G4+": 230, "KingTech K-85G4+": 300,
                    "KingTech K-86G4+": 300, "KingTech K-102G4+": 330,
                    "KingTech K-130G4+": 410, "KingTech K-142G4+": 440,
                    "KingTech K-160G4+": 490, "KingTech K-180G4+": 560,
                    "KingTech K-210G4+": 590, "KingTech K-235G4+": 680,
                    "KingTech K-260G4+": 760, "KingTech K-320G4+": 870,
                    "KingTech K-450G4+": 1100}

turbine_dic_temp = {"KingTech K-30G4+": 720, "KingTech K-45G4+": 720,
                    "KingTech K-55G4+": 730, "KingTech K-65G4+": 730,
                    "KingTech K-70G4+": 700, "KingTech K-85G4+": 700,
                    "KingTech K-86G4+": 700, "KingTech K-102G4+": 750,
                    "KingTech K-130G4+": 700, "KingTech K-142G4+": 750,
                    "KingTech K-160G4+": 700, "KingTech K-180G4+": 700,
                    "KingTech K-210G4+": 650, "KingTech K-235G4+": 750,
                    "KingTech K-260G4+": 700, "KingTech K-320G4+": 700,
                    "KingTech K-450G4+": 760}

turbine_dic_weight = {"KingTech K-30G4+": 450, "KingTech K-45G4+": 450,
                      "KingTech K-55G4+": 700, "KingTech K-65G4+": 600,
                      "KingTech K-70G4+": 720, "KingTech K-85G4+": 880,
                      "KingTech K-86G4+": 725, "KingTech K-102G4+": 910,
                      "KingTech K-130G4+": 1200, "KingTech K-142G4+": 1300,
                      "KingTech K-160G4+": 1540, "KingTech K-180G4+": 1540,
                      "KingTech K-210G4+": 1740, "KingTech K-235G4+": 2000,
                      "KingTech K-260G4+": 2200, "KingTech K-320G4+": 2900,
                      "KingTech K-450G4+": 4000}

turbine_dic_thrust = {"KingTech K-30G4+": 3, "KingTech K-45G4+": 4.5,
                      "KingTech K-55G4+": 5.5, "KingTech K-65G4+": 6.5,
                      "KingTech K-70G4+": 7, "KingTech K-85G4+": 8.5,
                      "KingTech K-86G4+": 8.6, "KingTech K-102G4+": 10,
                      "KingTech K-130G4+": 13, "KingTech K-142G4+": 14,
                      "KingTech K-160G4+": 16, "KingTech K-180G4+": 18,
                      "KingTech K-210G4+": 21, "KingTech K-235G4+": 23.5,
                      "KingTech K-260G4+": 26, "KingTech K-320G4+": 32,
                      "KingTech K-450G4+": 45}

turbine_dic_price = {"KingTech K-30G4+": 1590, "KingTech K-45G4+": 1690,
                    "KingTech K-55G4+": 1550, "KingTech K-65G4+": 1670,
                    "KingTech K-70G4+": 1790, "KingTech K-85G4+": 1890,
                    "KingTech K-86G4+": 1890, "KingTech K-102G4+": 2000,
                    "KingTech K-130G4+": 2250, "KingTech K-142G4+": 2450,
                    "KingTech K-160G4+": 2650, "KingTech K-180G4+": 2850,
                    "KingTech K-210G4+": 3150, "KingTech K-235G4+": 3350,
                    "KingTech K-260G4+": 3650, "KingTech K-320G4+": 4150,
                    "KingTech K-450G4+": 4500}

##These if-else statement determines with the user wants to use their own turbine for if ther want to use a turbine found within the catalog displayed for them

if turbine in turbine_list:
    print("Excellent! Great Choice!")
    turbine = turbine
    turbine_fuel = turbine_dic_fuel.get(turbine)
    turbine_temp = turbine_dic_temp.get(turbine)
    turbine_weight = turbine_dic_weight.get(turbine)
    turbine_thrust = turbine_dic_thrust.get(turbine)
    print( "You chose", turbine, "that consumes", turbine_fuel, "grams per minute , has a weight of", turbine_weight, "grams, has an exuast gas temperature of", turbine_temp, "and has", turbine_thrust, "kilograms of thrust.")
    
else:
    turbine = input("What turbine are you using?")
    turbine_fuel = float(input("What is the fuel consumption? (in g/min)"))
    turbine_temp = float(input("What is the exhuast gas temperature? (in Celcius)"))
    turbine_weight = float(input("What is the turbine weight? (in grams)"))
    turbine_thrust = float(input("What is the turbine thrust? (in kilograms)"))
    print( "You chose", turbine, "that consumes", turbine_fuel, "grams per minute , has a weight of", turbine_weight, "grams, has an exuast gas temperature of", turbine_temp, "and has", turbine_thrust, "kilograms of thrust.")

#final_list =[turbine, turbine_fuel, turbine_temp, turbine_weight, turbine_thrust]
jet_A1_fuel_weight = 0.804
conv_fuel_weight = jet_A1_fuel_weight / 1 #1 is the converstion factor from kg/L to g/ml, it can be changed for various conversion factors

plane_weight_shell = float(input("What is your shell/strcuture plane weight? (in kg)"))
fuel_cap = float(input("What is your fuel tank capacity? (in ml)"))
factor_of_saftey = float(input("State a factor of safety precentage as a decimal point for your flight time (Ex. 100% = 1, 80% = 0.8, etc):"))

#fun = 8
##These are the various functions that can be found in the functions and have been placed here for presentation viewing convenience

##def max_plane_flight_time(turbine_fuel, fuel_cap, turbine):
##    max_plane_f_time = fuel_cap / turbine_fuel
##    print("The flight time with", fuel_cap, "is", max_plane_f_time, "in a", turbine, ".")
##    return max_plane_f_time
##
##def safe_flight_time(factor_of_saftey, max_plane_f_time):
##    safe_f_t = max_plane_f_time * factor_of_saftey
##    print("Safe flight time accounting for fuel consumption is", safe_f_t, ".")
##    return safe_f_t
##
##def safe_flight_fuel(factor_of_saftey, fuel_cap):
##    safe_f_f = fuel_cap * factor_of_saftey
##    print("Safe flight fuel usage accounting for fuel consumption is", safe_f_f, ".")
##    return safe_f_f
##
##def fuel_usage_remain(fuel_cap, safe_f_f):
##    fuel_u_remain = fuel_cap - safe_f_f
##    print("Fuel remaining after landing:", safe_f_f)
##    return fuel_u_remain
##
##def fuel_weight (fuel_cap, conv_fuel_weight):
##    fuel_w = fuel_cap / conv_fuel_weight
##    print("Fuel weight at takeoff:", fuel_w)
##    return fuel_w
##
##def fuel_land_weight(fuel_u_remain, conv_fuel_weight):
##    fuel_l_w = fuel_u_remain / conv_fuel_weight
##    print("Fuel weight at landing:", fuel_l_w)
##    return fuel_l_w
##
##def plane_weight_tot(plane_weight_shell, fuel_w, turbine_weight):
##    plane_w_tot = plane_weight_shell + fuel_w + turbine_weight
##    print("The total takeoff plane weight is", plane_w_tot, ".")
##    return plane_w_tot
##
##def plane_weight_tot_land(plane_weight_shell, fuel_l_w, turbine_weight):
##    plane_w_land = plane_weight_shell + fuel_l_w + turbine_weight
##    print("The total landing plane weight is", plane_w_land, ".")
##    return plane_w_land

#File Creation
# 
equ = open("48975_6422577_7073927.txt", "w")

#Determine if additional information is wanted by the user
doc_ans = str(input("Do you want to run the parameters for all turbines in catalog and not your turbine? (yes or no)"))

##These will open a text document called flight_parameters                
equ = open("48975_6422577_7073927.txt", "a")

#doc_ans is the variable to question the user if they need all the data served in a text file for later
#reference so that the user doesn't have to go back and run the code again
if doc_ans == "no":
    
    max_plane_f_time = max_plane_flight_time(turbine_fuel, fuel_cap, turbine)
    safe_f_t = safe_flight_time(factor_of_saftey, max_plane_f_time)
    safe_f_f = safe_flight_fuel(factor_of_saftey, fuel_cap)
    fuel_u_remain = fuel_usage_remain(fuel_cap, safe_f_f)
    fuel_w = fuel_weight(fuel_cap, conv_fuel_weight)
    fuel_l_w = fuel_land_weight (fuel_u_remain, conv_fuel_weight)
    plane_w_tot = plane_weight_tot(plane_weight_shell, fuel_w, turbine_weight)
    plane_w_land = plane_weight_tot_land(plane_weight_shell, fuel_l_w, turbine_weight)
    
    equ.write(f"The flight time with {max_plane_f_time}. \n")
    equ.write(f"Safe flight time accounting for fuel consumption is {safe_f_t}.\n")
    equ.write(f"Safe flight fuel usage accounting for fuel consumption is {safe_f_f}.\n")
    equ.write(f"Fuel remaining after landing: {safe_f_f}\n")
    equ.write(f"Fuel weight at takeoff: {fuel_w}\n")
    equ.write(f"Fuel weight at landing: {fuel_l_w}\n")
    equ.write(f"The total takeoff plane weight is {plane_w_tot}.\n")
    equ.write(f"The total landing plane weight is {plane_w_land}.\n")

#If you don't want all parameters then say no if yes (or any other response) then all will be printed
else:
    for i in range(len(turbine_list)):
        turbine = turbine_list[i]
        turbine_fuel = turbine_dic_fuel.get(turbine)
        turbine_temp = turbine_dic_temp.get(turbine)
        turbine_weight = turbine_dic_weight.get(turbine)
        turbine_thrust = turbine_dic_thrust.get(turbine)
        print( "You chose", turbine, "that consumes", turbine_fuel, "grams per minute , has a weight of", turbine_weight, "grams, has an exuast gas temperature of", turbine_temp, "and has", turbine_thrust, "kilograms of thrust.")

        max_plane_f_time = max_plane_flight_time(turbine_fuel, fuel_cap, turbine)
        safe_f_t = safe_flight_time(factor_of_saftey, max_plane_f_time)
        safe_f_f = safe_flight_fuel(factor_of_saftey, fuel_cap)
        fuel_u_remain = fuel_usage_remain(fuel_cap, safe_f_f)
        fuel_w = fuel_weight(fuel_cap, conv_fuel_weight)
        fuel_l_w = fuel_land_weight (fuel_u_remain, conv_fuel_weight)
        plane_w_tot = plane_weight_tot(plane_weight_shell, fuel_w, turbine_weight)
        plane_w_land = plane_weight_tot_land(plane_weight_shell, fuel_l_w, turbine_weight)
        
        equ.write(f"The flight time with {max_plane_f_time}. \n")
        equ.write(f"Safe flight time accounting for fuel consumption is {safe_f_t}.\n")
        equ.write(f"Safe flight fuel usage accounting for fuel consumption is {safe_f_f}.\n")
        equ.write(f"Fuel remaining after landing: {safe_f_f}\n")
        equ.write(f"Fuel weight at takeoff: {fuel_w}\n")
        equ.write(f"Fuel weight at landing: {fuel_l_w}\n")
        equ.write(f"The total takeoff plane weight is {plane_w_tot}.\n")
        equ.write(f"The total landing plane weight is {plane_w_land}.\n")

##Close the text file
equ.close()


##var_list = [turbine_dic_fuel, turbine_dic_weight, turbine_dic_thrust, turbine_dic_temp, turbine_dic_price]


bar_arr_turbine = np.array(turbine_list)
##print(bar_arr_turbine)

turbine_fuel_arr = []
turbine_weight_arr = []
turbine_thrust_arr = []
turbine_thrust_arr = []
turbine_temp_arr = []
turbine_price_arr = []
    
##new_list_arr = [turbine_fuel_arr, turbine_weight_arr, turbine_thrust_arr, turbine_temp_arr, turbine_price_arr]

#Parameters for the spacing of the bar graphs
num = len(turbine_list)
ind = np.arange(num)
width_bar = 0.20

#Creation of the arrays by creating lists from the dictionary values then making them numpy arrays
turbine_fuel_arr = np.array(list(turbine_dic_fuel.values()))
turbine_weight_arr = np.array(list(turbine_dic_weight.values()))
turbine_thrust_arr = np.array(list(turbine_dic_thrust.values()))
turbine_temp_arr = np.array(list(turbine_dic_temp.values()))
turbine_price_arr = np.array(list(turbine_dic_price.values()))

#Question the user on the type of graph display that they want, if yes to both then both will execute
bar_graph_response = input("Do you want to compare all of the turbines and their values (temp, fuel consumption, price, etc.) in a bar graph display? (yes or no) ")
bar_graph_dis = input("Do you want to compare all turbines under one parameter(value)? (yes or no) ")

#If-elif-elif-else statement to execute on the above responses from the user
if bar_graph_response == "yes" and bar_graph_dis == "no":
    #Bar creation with spacing, label and color
    bar_1 = plt.bar(ind, turbine_thrust_arr, width_bar, label = 'Thrust', color = 'green')
    bar_2 = plt.bar(ind + width_bar, turbine_fuel_arr, width_bar, label = 'Fuel Consumption', color = 'red')
    bar_3 = plt.bar(ind + width_bar*2, turbine_weight_arr, width_bar, label = 'Weight', color = 'blue')
    bar_4 = plt.bar(ind + width_bar*3, turbine_temp_arr, width_bar, label = 'Temperature', color = 'yellow')
    bar_5 = plt.bar(ind + width_bar*4, turbine_price_arr, width_bar, label = 'Price', color = 'orange')
    #Plot modification
    plt.title('Full Trade Study Display')
    plt.xlabel('Turbines')
    plt.ylabel('Values')
    plt.legend()
    plt.xticks(rotation = 45)
    plt.xticks(ind)
    
    plt.show()
    
elif bar_graph_response == "yes" and bar_graph_dis == "yes":
    #Creation of the arrays using the list function to convert the dic values into list "arrays"
    turbine_fuel_arr = list(turbine_dic_fuel.values())
    turbine_weight_arr = list(turbine_dic_weight.values())
    turbine_thrust_arr = list(turbine_dic_thrust.values())
    turbine_temp_arr = list(turbine_dic_temp.values())
    turbine_price_arr = list(turbine_dic_price.values())
    #figure creation for use of the axes to create subplots on one figure
    fig, bar_set = plt.subplots(3, 2, figsize= (35, 60))
    
    bar_set[0][0].bar(ind, turbine_thrust_arr, width_bar, label = 'Thrust', color = 'green')
    bar_set[0][0].bar(ind + width_bar, turbine_fuel_arr, width_bar, label = 'Fuel Consumption', color = 'red')
    bar_set[0][0].bar(ind + width_bar*2, turbine_weight_arr, width_bar, label = 'Weight', color = 'blue')
    bar_set[0][0].bar(ind + width_bar*3, turbine_temp_arr, width_bar, label = 'Temperature', color = 'yellow')
    bar_set[0][0].bar(ind + width_bar*4, turbine_price_arr, width_bar, label = 'Price', color = 'orange')
    bar_set[0][0].set_title('Full Trade Study Display')     #Plot modification
    bar_set[0][0].set_xlabel('Turbines')
    bar_set[0][0].set_ylabel('Values')
    bar_set[0][0].set_xticks(ind)
    bar_set[0][0].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[0][0].legend()

    bar_set[0][1].bar(ind, turbine_thrust_arr, width_bar, label = 'Thrust', color = 'green')
    bar_set[0][1].set_title('Thrust Trade Study')
    bar_set[0][1].set_xlabel('Turbines')
    bar_set[0][1].set_ylabel('Thrust')
    bar_set[0][1].set_xticks(ind)
    bar_set[0][1].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[0][1].legend()

    bar_set[1][0].bar(ind, turbine_fuel_arr, width_bar, label = 'Fuel Consumption', color = 'green')
    bar_set[1][0].set_title('Fuel Consumption Trade Study')
    bar_set[1][0].set_xlabel('Turbines')
    bar_set[1][0].set_ylabel('Fuel Consumption')
    bar_set[1][0].set_xticks(ind)
    bar_set[1][0].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[1][0].legend()

    bar_set[1][1].bar(ind, turbine_weight_arr, width_bar, label = 'Weight', color = 'green')
    bar_set[1][1].set_title('Weight Trade Study')
    bar_set[1][1].set_xlabel('Turbines')
    bar_set[1][1].set_ylabel('Weight')
    bar_set[1][1].set_xticks(ind)
    bar_set[1][1].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[1][1].legend()

    bar_set[2][0].bar(ind, turbine_temp_arr, width_bar, label = 'Temperature', color = 'green')
    bar_set[2][0].set_title('Temperature Trade Study')
    bar_set[2][0].set_xlabel('Turbines')
    bar_set[2][0].set_ylabel('Temperature')
    bar_set[2][0].set_xticks(ind)
    bar_set[2][0].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[2][0].legend()

    bar_set[2][1].bar(ind, turbine_price_arr, width_bar, label = 'Price', color = 'green')
    bar_set[2][1].set_title('Price Trade Study')
    bar_set[2][1].set_xlabel('Turbines')
    bar_set[2][1].set_ylabel('Price')
    bar_set[2][1].set_xticks(ind)
    bar_set[2][1].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[2][1].legend()


    
    plt.show()
    
elif bar_graph_response == "no" and bar_graph_dis == "yes":

    
    turbine_fuel_arr = list(turbine_dic_fuel.values())
    turbine_weight_arr = list(turbine_dic_weight.values())
    turbine_thrust_arr = list(turbine_dic_thrust.values())
    turbine_temp_arr = list(turbine_dic_temp.values())
    turbine_price_arr = list(turbine_dic_price.values())
    
    fig, bar_set = plt.subplots(3, 2, figsize= (35, 60))


    bar_set[0][0].bar(ind, turbine_thrust_arr, width_bar, label = 'Thrust', color = 'green')
    bar_set[0][0].set_title('Thrust Trade Study')
    bar_set[0][0].set_xlabel('Turbines')
    bar_set[0][0].set_ylabel('Values')
    bar_set[0][0].set_xticks(ind)
    bar_set[0][0].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[0][0].legend()

    bar_set[0][1].bar(ind, turbine_fuel_arr, width_bar, label = 'Fuel Consumption', color = 'green')
    bar_set[0][1].set_title('Fuel Consumption Trade Study')
    bar_set[0][1].set_xlabel('Turbines')
    bar_set[0][1].set_ylabel('Fuel Consumption')
    bar_set[0][1].set_xticks(ind)
    bar_set[0][1].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[0][1].legend()

    bar_set[1][0].bar(ind, turbine_weight_arr, width_bar, label = 'Weight', color = 'green')
    bar_set[1][0].set_title('Weight Trade Study')
    bar_set[1][0].set_xlabel('Turbines')
    bar_set[1][0].set_ylabel('Weight')
    bar_set[1][0].set_xticks(ind)
    bar_set[1][0].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[1][0].legend()

    bar_set[1][1].bar(ind, turbine_temp_arr, width_bar, label = 'Temperature', color = 'green')
    bar_set[1][1].set_title('Temperature Trade Study')
    bar_set[1][1].set_xlabel('Turbines')
    bar_set[1][1].set_ylabel('Temperature')
    bar_set[1][1].set_xticks(ind)
    bar_set[1][1].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[1][1].legend()

    bar_set[2][1].bar(ind, turbine_price_arr, width_bar, label = 'Price', color = 'green')
    bar_set[2][1].set_title('Price Trade Study')
    bar_set[2][1].set_xlabel('Turbines')
    bar_set[2][1].set_ylabel('Price')
    bar_set[2][1].set_xticks(ind)
    bar_set[2][1].set_xticklabels(bar_arr_turbine, rotation = 45)
    bar_set[2][1].legend()
    
    plt.show()
        
else:
    print("No plots,  that's ok. Happy to help come back again!")
    
print("Thank you for using our services! Come back again!")


##These are trail run iterations to execute my project but they failed
##I tried to use nested for loops to generate lists that would then be converted to arrays
##with new names signaling that they are arrays but I failed at creating them, it was way too complicated

##for b in new_list_arr:
##for i in range(len(turbine_list)):
##for c in var_list:
##    value_list = list(c.values())
##    index = var_list.index(c)
##    new_list_arr[index] = value_list
##        
##        
##    print(new_list_arr[index])
##print(turbine_fuel_arr)

    


##var_list = [turbine_dic_fuel, turbine_dic_weight, turbine_dic_thrust, turbine_dic_temp, turbine_dic_price]
##
##new_list_arr = [turbine_fuel_arr, turbine_weight_arr, turbine_thrust_arr, turbine_temp_arr, turbine_price_arr]
##
##new_list_arr[b] = value_list[b]            


    

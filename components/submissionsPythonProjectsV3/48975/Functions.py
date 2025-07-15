#List of nesscary equations for Turbine Project
# 48975_6422576_328076
def max_plane_flight_time(turbine_fuel, fuel_cap, turbine):
    max_plane_f_time = fuel_cap / turbine_fuel
    print("The flight time with", fuel_cap, "is", max_plane_f_time, "in a", turbine, ".")
    return max_plane_f_time

def safe_flight_time(factor_of_saftey, max_plane_f_time):
    safe_f_t = max_plane_f_time * factor_of_saftey
    print("Safe flight time accounting for fuel consumption is", safe_f_t, ".")
    return safe_f_t

def safe_flight_fuel(factor_of_saftey, fuel_cap):
    safe_f_f = fuel_cap * factor_of_saftey
    print("Safe flight fuel usage accounting for fuel consumption is", safe_f_f, ".")
    return safe_f_f

def fuel_usage_remain(fuel_cap, safe_f_f):
    fuel_u_remain = fuel_cap - safe_f_f
    print("Fuel remaining after landing:", safe_f_f)
    return fuel_u_remain

def fuel_weight (fuel_cap, conv_fuel_weight):
    fuel_w = fuel_cap / conv_fuel_weight
    print("Fuel weight at takeoff:", fuel_w)
    return fuel_w

def fuel_land_weight(fuel_u_remain, conv_fuel_weight):
    fuel_l_w = fuel_u_remain / conv_fuel_weight
    print("Fuel weight at landing:", fuel_l_w)
    return fuel_l_w

def plane_weight_tot(plane_weight_shell, fuel_w, turbine_weight):
    plane_w_tot = plane_weight_shell + fuel_w + turbine_weight
    print("The total takeoff plane weight is", plane_w_tot, ".")
    return plane_w_tot

def plane_weight_tot_land(plane_weight_shell, fuel_l_w, turbine_weight):
    plane_w_land = plane_weight_shell + fuel_l_w + turbine_weight
    print("The total landing plane weight is", plane_w_land, ".")
    return plane_w_land

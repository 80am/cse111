#at the top of the file I gave the fixed numbers variables so that I could call the variables instead of stating number. Thus the code is easier to read when trying to follow along.

earth_acceleration_of_gravity = 9.80665
water_density = 998.2
water_dynamic_viscosity = 0.0010016


def water_column_height(tower_height, tank_height):

# h is height of the water column
# t is the height of the tower
# w is the height of the walls of the tank that is on top of the tower

    t = tower_height
    w = tank_height

    h = t + ((3*w)/4)

    return h


def pressure_gain_from_water_height(height):

    # P is the pressure in kilopascals
    # ρ is the density of water (998.2 kilogram / meter3)
    # g is the acceleration from Earths gravity (9.80665 meter / second2)
    # h is the height of the water column in meters

#     Name	Value
# EARTH_ACCELERATION_OF_GRAVITY	9.80665
# WATER_DENSITY	998.2
# WATER_DYNAMIC_VISCOSITY	0.0010016


    p = water_density
    g = earth_acceleration_of_gravity
    h = height


    P = (p*g*h)/1000

    return P 


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    
# P is the lost pressure in kilopascals
# f is the pipe’s friction factor
# L is the length of the pipe in meters
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the pipe in meters / second
# d is the diameter of the pipe in meters

    f = friction_factor
    L = pipe_length
    p = water_density
    v = fluid_velocity
    d = pipe_diameter

    # P = ((-f)*L*p*(v**)) / (2000*d)
    P = (-f)*L*p*(v*v)/(2000*d)

    return P

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):

# P is the lost pressure in kilopascals
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the pipe in meters / second
# n is the quantity of fittings

    p = water_density
    v = fluid_velocity
    n = quantity_fittings

    P = ((-0.04*p)*(v*v)*n)/2000

    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):

# R is the Reynolds number
# ρ is the density of water (998.2 kilogram / meter3)
# d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
# v is the velocity of the water flowing through the pipe in meters / second
# μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

# Name	Value
# EARTH_ACCELERATION_OF_GRAVITY	9.80665
# WATER_DENSITY	998.2
# WATER_DYNAMIC_VISCOSITY	0.0010016




    p = water_density
    d = hydraulic_diameter
    v = fluid_velocity
    u = water_dynamic_viscosity

    R = (p*d*v)/u

    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):

# k is a constant computed by the first formula and used in the second formula
# R is the Reynolds number that corresponds to the pipe with the larger diameter
# D is the diameter of the larger pipe in meters
# d is the diameter of the smaller pipe in meters
# P is the lost pressure kilopascals
# ρ is the density of water (998.2 kilogram / meter3)
# v is the velocity of the water flowing through the larger diameter pipe in meters / second

    R = reynolds_number
    D = larger_diameter
    d = smaller_diameter
    p = water_density
    v = fluid_velocity

    k = (0.1+(50/R))*((D/d)**4-1)

    P = (-k*p*(v**2))/2000

    return P

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
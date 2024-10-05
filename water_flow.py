def water_column_height(tower_height, tank_height):
    #Calculate the height of a column of water from tower height and tank wall height.
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    #Calculate the pressure caused by Earth's gravity pulling on the water stored in an elevated tank.
    # Constants
    WATER_DENSITY = 998.2
    GRAVITY = 9.80665
    
    # Calculate pressure in kilopascals
    pressure = (WATER_DENSITY * GRAVITY * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    #Calculate the water pressure lost due to friction between water and pipe walls.
    # Constants
    WATER_DENSITY = 998.2
    
    # Calculate pressure loss in kilopascals
    pressure_loss = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss
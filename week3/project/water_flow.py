"""
Author: Kevin Cross Minchakpu
Description: Calculates water flow, pressure gains from water towers, 
             and fluid pressure losses through pipes and fittings.
"""

# Constants
PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)

SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75             # (meters / second)
WATER_DENSITY = 998.2                # density of water (kilogram / meter^3)
WATER_DYNAMIC_VISCOSITY = 0.0010016  # dynamic viscosity of water (Pascal seconds)

def main() -> None:
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
    
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    
    print(f"Pressure at house: {pressure:.1f} kilopascals")

def water_column_height(tower_height: float, tank_height: float) -> float:
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height: float) -> float:
    gravity = 9.80665
    return (WATER_DENSITY * gravity * height) / 1000

def pressure_loss_from_pipe(pipe_diameter: float, pipe_length: float, friction_factor: float, fluid_velocity: float) -> float:
    # Uses 2000 for standard kPa dynamic metric balancing
    return (-friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity: float, quantity_fittings: int) -> float:
    return (-0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter: float, fluid_velocity: float) -> float:
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter: float, fluid_velocity: float, reynolds_number: float, smaller_diameter: float) -> float:
    if reynolds_number == 0:
        return 0.0
    k = (0.1 + 50 / reynolds_number) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    return (-k * WATER_DENSITY * (fluid_velocity ** 2)) / 2000

if __name__ == "__main__":
    main()
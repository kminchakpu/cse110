# Author: Kevin Cross Minchakpu
# Course: CSE 111 - Block 3
# Institution: Brigham Young University - Idaho
# Instructor: CJ Waisath

"""
Enhancements added:
1. Defined global constants outside the functions for Earth's acceleration 
   of gravity, water density, and water dynamic viscosity to improve 
   maintainability.
2. Added a conversion function (convert_kpa_to_psi) to convert the final 
   calculated pressure from kilopascals to pounds per square inch (psi) 
   and printed both values in the main block.
"""

import math

# Global Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height: float, tank_height: float) -> float:
    """Calculates the height of the water column."""
    # h = t + (3 * w) / 4
    return tower_height + (3 * tank_height) / 4


def pressure_gain_from_water_height(height: float) -> float:
    """Calculates the pressure gain in kPa from the water column height."""
    # P = (rho * g * h) / 1000
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000


def pressure_loss_from_pipe(
    pipe_diameter: float, pipe_length: float, friction_factor: float, fluid_velocity: float
) -> float:
    """Calculates the pressure loss in kPa due to friction within a pipe."""
    # P = (-f * L * rho * v^2) / (2000 * d)
    numerator = -friction_factor * pipe_length * WATER_DENSITY * (fluid_velocity ** 2)
    denominator = 2000 * pipe_diameter
    return numerator / denominator


def pressure_loss_from_fittings(fluid_velocity: float, quantity_fittings: int) -> float:
    """Calculates the pressure loss in kPa from pipe fittings (e.g., 90-degree elbows)."""
    # P = (-0.04 * rho * v^2 * n) / 2000
    numerator = -0.04 * WATER_DENSITY * (fluid_velocity ** 2) * quantity_fittings
    return numerator / 2000


def reynolds_number(hydraulic_diameter: float, fluid_velocity: float) -> float:
    """Calculates the dimensionless Reynolds number for fluid flow."""
    # R = (rho * d * v) / mu
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY


def pressure_loss_from_pipe_reduction(
    larger_diameter: float, fluid_velocity: float, reynolds_number: float, smaller_diameter: float
) -> float:
    """Calculates the pressure loss in kPa caused by a reduction in pipe diameter."""
    if reynolds_number == 0:
        return 0.0
    
    # k = (0.1 + 50 / R) * ((D / d)^4 - 1)
    k = (0.1 + 50 / reynolds_number) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    
    # P = (-k * rho * v^2) / 2000
    return (-k * WATER_DENSITY * (fluid_velocity ** 2)) / 2000


def convert_kpa_to_psi(kpa_value: float) -> float:
    """Converts a pressure value from kilopascals (kPa) to pounds per square inch (psi)."""
    # 1 kPa is approximately 0.1450377377 psi
    return kpa_value * 0.1450377377


def main() -> None:
    """Collects inputs from the user, computes total system pressure, and outputs results."""
    print("Water Flow Design Program")
    print("-------------------------")
    
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    supply_length = float(input("Length of supply pipe from tank to lot (meters): "))
    num_fittings = int(input("Number of 90° angles in supply pipe: "))
    house_length = float(input("Length of pipe from supply to house (meters): "))

    # Calculate water column height and initial pressure gain
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    # Hardcoded project engineering dimensions for the main supply pipe flow
    # (Provided in the full main function template)
    v_supply = 1.65
    d_supply = 0.28687
    f_supply = 0.013

    # Main pipe losses
    loss_pipe1 = pressure_loss_from_pipe(d_supply, supply_length, f_supply, v_supply)
    loss_fit1 = pressure_loss_from_fittings(v_supply, num_fittings)
    
    # Hardcoded project engineering dimensions for the house pipe flow
    v_house = 1.75
    d_house = 0.048692
    f_house = 0.018
    
    # Loss from pipe reduction
    r_num = reynolds_number(d_supply, v_supply)
    loss_reduction = pressure_loss_from_pipe_reduction(d_supply, v_supply, r_num, d_house)
    
    # House pipe losses
    loss_pipe2 = pressure_loss_from_pipe(d_house, house_length, f_house, v_house)

    # Accumulate all network losses
    pressure += loss_pipe1 + loss_fit1 + loss_reduction + loss_pipe2

    # Output final results in both metric and imperial units
    print(f"\nPressure at house: {pressure:.1f} kilopascals")
    psi_pressure = convert_kpa_to_psi(pressure)
    print(f"Pressure at house: {psi_pressure:.1f} psi")


if __name__ == "__main__":
    main()
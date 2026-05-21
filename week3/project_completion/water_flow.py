"""
Author: Kevin Cross Minchakpu

Enhancements:
- Added constants for gravity and water properties.
- Added a function to convert kilopascals (kPa) to pounds per square inch (psi).
- Program now displays final pressure in both kPa and psi.
"""

# Constants
PVC_SCHED80_INNER_DIAMETER = 0.28687
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65

HDPE_SDR11_INNER_DIAMETER = 0.048692
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75

WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016
EARTH_ACCELERATION_OF_GRAVITY = 9.80665


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

    pressure += pressure_loss_from_pipe(
        diameter, length1, friction, velocity
    )

    pressure += pressure_loss_from_fittings(
        velocity, quantity_angles
    )

    pressure += pressure_loss_from_pipe_reduction(
        diameter,
        velocity,
        reynolds,
        HDPE_SDR11_INNER_DIAMETER
    )

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY

    pressure += pressure_loss_from_pipe(
        diameter, length2, friction, velocity
    )

    psi = kpa_to_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi:.1f} psi")


def water_column_height(
        tower_height: float,
        tank_height: float
    ) -> float:

    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height: float) -> float:

    return (
        WATER_DENSITY
        * EARTH_ACCELERATION_OF_GRAVITY
        * height
        / 1000
    )


def pressure_loss_from_pipe(
        pipe_diameter: float,
        pipe_length: float,
        friction_factor: float,
        fluid_velocity: float
    ) -> float:

    return (
        -friction_factor
        * pipe_length
        * WATER_DENSITY
        * fluid_velocity**2
        / (2000 * pipe_diameter)
    )


def pressure_loss_from_fittings(
        fluid_velocity: float,
        quantity_fittings: int
    ) -> float:

    return (
        -0.04
        * WATER_DENSITY
        * fluid_velocity**2
        * quantity_fittings
        / 2000
    )


def reynolds_number(
        hydraulic_diameter: float,
        fluid_velocity: float
    ) -> float:

    return (
        WATER_DENSITY
        * hydraulic_diameter
        * fluid_velocity
        / WATER_DYNAMIC_VISCOSITY
    )


def pressure_loss_from_pipe_reduction(
        larger_diameter: float,
        fluid_velocity: float,
        reynolds_number_value: float,
        smaller_diameter: float
    ) -> float:

    if reynolds_number_value == 0:
        return 0

    k = (
        0.1
        + (50 / reynolds_number_value)
    ) * (
        (larger_diameter / smaller_diameter) ** 4 - 1
    )

    return (
        -k
        * WATER_DENSITY
        * fluid_velocity**2
        / 2000
    )


def kpa_to_psi(kpa: float) -> float:
    return kpa * 0.145038


if __name__ == "__main__":
    main()
# Author: Kevin Cross Minchakpu
# Course: CSE 111 - Block 3
# Institution: Brigham Young University - Idaho
# Instructor: CJ Waisath

"""This program calculates the storage and cost efficiency of various steel can sizes based on their dimensions and cost. It defines functions to compute the volume and surface area of a cylinder, as well as the storage and cost efficiency. The results are printed for each can size in a formatted manner."""

import math

def main():
    # List of can data: [Name, Radius, Height, Cost]
    can_sizes = [
        ["#1 Picnic", 6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]

    best_storage_name: str = ""
    max_storage_efficiency: float = -1.0

    best_cost_name: str = ""
    max_cost_efficiency: float = -1.0

    for can in can_sizes:
        name: str = can[0]
        radius: float = can[1]
        height: float = can[2]
        cost: float = can[3]

        storage_eff: float = compute_storage_efficiency(radius, height)
        cost_eff: float = compute_cost_efficiency(radius, height, cost)

        print(f"{name} Storage: {storage_eff:.2f}, Cost: {cost_eff:.2f}")

        # Determine which can size has the best storage efficiency
        if storage_eff > max_storage_efficiency:
            max_storage_efficiency = storage_eff
            best_storage_name = name

        # Determine which can size has the best cost efficiency
        if cost_eff > max_cost_efficiency:
            max_cost_efficiency = cost_eff
            best_cost_name = name

    print("-" * 30)
    print(f"Best Storage Efficiency: {best_storage_name} ({max_storage_efficiency:.2f})")
    print(f"Best Cost Efficiency: {best_cost_name} ({max_cost_efficiency:.2f})")

def compute_volume(radius: float, height: float) -> float:
    """Compute and return the volume of a cylinder."""
    return math.pi * (radius ** 2) * height

def compute_surface_area(radius: float, height: float) -> float:
    """Compute and return the surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius: float, height: float) -> float:
    """Compute and return the storage efficiency of a steel can size."""
    volume: float = compute_volume(radius, height)
    surface_area: float = compute_surface_area(radius, height)
    return volume / surface_area

def compute_cost_efficiency(radius: float, height: float, cost: float) -> float:
    """Compute and return the volume of a steel can divided by its cost."""
    volume: float = compute_volume(radius, height)
    return volume / cost

if __name__ == "__main__":
    main()
"""
Author: Kevin Cross Minchakpu
Course: CSE 111 [Programming with Functions]
Instructor: CJ Waisaith

Purpose: Community Health Data Analyzer and Visualizer
Description: Processes regional community health datasets to calculate risk scores,
             filter high-priority districts, and generate visual summaries.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from tabulate import tabulate

def load_health_data(file_path: str) -> pd.DataFrame:
    """
    Safely loads a CSV file into a pandas DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file data path '{file_path}' does not exist.")
    
    # Read the data, ensuring the header is parsed correctly
    df = pd.read_csv(file_path)
    return df

def calculate_risk_score(incidence_rate: float, prevention_rate: float) -> float:
    """
    Calculates a localized priority risk score based on disease incidence 
    and community prevention/vaccination coverage.
    
    Formula: Risk = Incidence Rate * (1.0 - Prevention Rate)
    """
    if incidence_rate < 0 or prevention_rate < 0:
        raise ValueError("Rates cannot be negative values.")
        
    # Standardize prevention rate scale if provided as a percentage out of 100
    if prevention_rate > 1.0:
        prevention_rate = prevention_rate / 100.0
        
    risk_score = incidence_rate * (1.0 - prevention_rate)
    return round(risk_score, 2)

def filter_high_priority_zones(data: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Filters the DataFrame to return only rows where the 'Calculated_Risk' 
    exceeds the given threshold.
    """
    if "Calculated_Risk" not in data.columns:
        # Programmatically apply the risk score calculation across the dataframe rows
        data["Calculated_Risk"] = data.apply(
            lambda row: calculate_risk_score(row["Incidence_Rate"], row["Prevention_Rate"]), 
            axis=1
        )
        
    filtered_df = data[data["Calculated_Risk"] >= threshold]
    return filtered_df.sort_values(by="Calculated_Risk", ascending=False)

def generate_health_summary_chart(data: pd.DataFrame, output_image_path: str) -> None:
    """
    Generates a bar chart visualizing the high-risk districts with dynamic colors.
    """
    if data.empty:
        print("No high priority data found to plot.")
        return

    plt.figure(figsize=(10, 6))
    
    # Create a list of colors based on the risk score value
    bar_colors = []
    for score in data["Calculated_Risk"]:
        if score >= 50:
            bar_colors.append("crimson")     # Extreme Risk
        elif score >= 30:
            bar_colors.append("darkorange")  # High Risk
        else:
            bar_colors.append("dodgerblue")  # Moderate Risk

    # Pass the list of colors into the bar chart function
    plt.bar(data["District"], data["Calculated_Risk"], color=bar_colors, edgecolor="black")
    
    plt.title("Public Health Intervention Priority Zones", fontsize=14, fontweight="bold")
    plt.xlabel("Districts / Communities", fontsize=12)
    plt.ylabel("Calculated Risk Score", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    
    plt.savefig(output_image_path)
    plt.close()
    print(f"Visualization saved successfully with dynamic colors to: {output_image_path}")

def main() -> None:
    """
    Orchestrates the program flow, handles user text input, and displays results.
    """
    print("=== Community Health Data Analyzer ===")
    file_path = input("Enter the path to the health CSV data file: ").strip()
    
    try:
        # Load data
        health_data = load_health_data(file_path)
        print("\nData loaded successfully!")
        print(health_data.head())
        
        # Process data and filter risk zones
        threshold = float(input("\nEnter the minimum Risk Score threshold for intervention (e.g., 15.0): "))
        priority_zones = filter_high_priority_zones(health_data, threshold)
        
        # Output results
        print(f"\n--- HIGH INTERVENTION PRIORITY ZONES (Risk >= {threshold}) ---")
        if priority_zones.empty:
            print("Great news! No districts exceed this risk threshold.")
        else:
            print(tabulate(priority_zones[["District", "Incidence_Rate", "Prevention_Rate", "Calculated_Risk"]], headers="keys", tablefmt="grid"))
            
            # Generate and save the chart visualization
            chart_filename = "high_risk_zones_summary.png"
            generate_health_summary_chart(priority_zones, chart_filename)
            
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Data Processing Error: {val_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
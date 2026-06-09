"""
Author: Kevin Cross Minchakpu
Purpose: Unit tests for health analyzer functions using pytest.
"""

import pytest
import pandas as pd
from health_analyzer import calculate_risk_score, filter_high_priority_zones

def test_calculate_risk_score():
    """
    Verifies that risk calculations are correct based on incidence and prevention rates.
    """
    # Test typical cases
    assert calculate_risk_score(50.0, 0.20) == 40.0  
    assert calculate_risk_score(100.0, 0.75) == 25.0  
    
    # Test handling of prevention percentages scaled out of 100
    assert calculate_risk_score(50.0, 20.0) == 40.0   
    
    # Test edge case: perfect prevention
    assert calculate_risk_score(80.0, 1.0) == 0.0
    
    # Test input validation errors
    with pytest.raises(ValueError):
        calculate_risk_score(-10.0, 0.5)

def test_filter_high_priority_zones():
    """
    Verifies that the dataframe filtering accurately captures only rows above the threshold.
    """
    # Setup a mock pandas DataFrame to test logic
    mock_data = pd.DataFrame({
        "District": ["Zone_1", "Zone_2", "Zone_3"],
        "Incidence_Rate": [10.0, 100.0, 50.0],
        "Prevention_Rate": [0.90, 0.20, 0.50]
    })
    
    # Calculated risks will be:
    # Zone_1: 10 * 0.1 = 1.0
    # Zone_2: 100 * 0.8 = 80.0
    # Zone_3: 50 * 0.5 = 25.0
    
    # Filter with a threshold of 20.0
    result_df = filter_high_priority_zones(mock_data, 20.0)
    
    # Assertions
    assert len(result_df) == 2
    assert "Zone_2" in result_df["District"].values
    assert "Zone_3" in result_df["District"].values
    assert "Zone_1" not in result_df["District"].values
    
    # Verify that it sorts from highest risk down to lowest risk
    first_row_district = result_df.iloc[0]["District"]
    assert first_row_district == "Zone_2"
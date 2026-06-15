import os
import pandas as pd
import pytest
from pathlib import Path
from health_analyzer import (
    load_health_data,
    calculate_risk_score,
    filter_high_priority_zones,
    generate_health_summary_chart
)

# Tests for load_health_data # 

def test_load_health_data_success(tmp_path: Path) -> None:
    """Verifies that a valid CSV file loads into a pandas DataFrame correctly."""
    # Setup temporary CSV file
    csv_file = tmp_path / "test_data.csv"
    csv_file.write_text("District,Incidence_Rate,Prevention_Rate\nDistrict A,45.0,0.2")
    
    # Execute
    df: pd.DataFrame = load_health_data(str(csv_file))
    
    # Assert
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 3)
    assert df.loc[0, "District"] == "District A"


def test_load_health_data_file_not_found() -> None:
    """Verifies FileNotFoundError is raised when a path does not exist."""
    fake_path: str = "non_existent_file_path_xyz.csv"
    with pytest.raises(FileNotFoundError, match="does not exist"):
        load_health_data(fake_path)


# Tests for calculate_risk_score 

@pytest.mark.parametrize(
    "incidence, prevention, expected_risk",
    [
        (50.0, 0.20, 40.0),    
        (50.0, 20.0, 40.0),    
        (10.0, 1.0, 0.0),      
        (100.0, 0.0, 100.0),   
        (45.5, 0.125, 39.81)   
    ]
)
def test_calculate_risk_score_valid_inputs(incidence: float, prevention: float, expected_risk: float) -> None:
    """Validates math processing, rounding, and percentage conversion scaling."""
    score: float = calculate_risk_score(incidence, prevention)
    assert score == expected_risk


def test_calculate_risk_score_negative_values() -> None:
    """Verifies ValueError is thrown when passing negative rates."""
    with pytest.raises(ValueError, match="Rates cannot be negative values."):
        calculate_risk_score(-10.0, 0.5)
    
    with pytest.raises(ValueError, match="Rates cannot be negative values."):
        calculate_risk_score(10.0, -0.5)


# Tests for filter_high_priority_zones

def test_filter_high_priority_zones_adds_column_and_filters() -> None:
    """Checks if Calculated_Risk is added, threshold applied, and descending sorted."""
    raw_data: dict[str, list[str] | list[float]] = {
        "District": ["District A", "District B", "District C"],
        "Incidence_Rate": [10.0, 50.0, 100.0],
        "Prevention_Rate": [0.0, 0.5, 0.2]  # Risks: A=10.0, B=25.0, C=80.0
    }
    df: pd.DataFrame = pd.DataFrame(raw_data)
    
    # Filter with a threshold of 25.0 (Should include C and B, drop A)
    filtered_df: pd.DataFrame = filter_high_priority_zones(df, 25.0)
    
    assert "Calculated_Risk" in filtered_df.columns
    assert len(filtered_df) == 2
    
    # Verify sorting order (Highest risk first)
    districts: list[str] = filtered_df["District"].tolist()
    assert districts == ["District C", "District B"]


# Tests for generate_health_summary_chart

def test_generate_health_summary_chart_creates_file(tmp_path: Path) -> None:
    """Confirms matplotlib successfully handles data and saves the output file."""
    chart_file: Path = tmp_path / "test_chart.png"
    
    # Mock data capturing all 3 dynamic color thresholds (>=50, >=30, <30)
    mock_data: dict[str, list[str] | list[float]] = {
        "District": ["High", "Medium", "Low"],
        "Calculated_Risk": [60.0, 35.0, 15.0]
    }
    df: pd.DataFrame = pd.DataFrame(mock_data)
    
    generate_health_summary_chart(df, str(chart_file))
    
    # This ensures file generation completely finished and saved
    assert chart_file.exists()
    assert chart_file.stat().st_size > 0


def test_generate_health_summary_chart_empty_data(tmp_path: Path) -> None:
    """Verifies that an empty DataFrame short-circuits gracefully without crashing."""
    chart_file: Path = tmp_path / "should_not_exist.png"
    df: pd.DataFrame = pd.DataFrame(columns=["District", "Calculated_Risk"])
    
    generate_health_summary_chart(df, str(chart_file))
    
    assert not chart_file.exists()
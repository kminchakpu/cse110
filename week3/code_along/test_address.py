from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that extract_city correctly isolates the city name."""
    # Standard format test
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    
    # Test with a multi-word city name
    assert extract_city("1600 Pennsylvania Ave NW, Washington, DC 20500") == "Washington"
    
    # Test with a different region style
    assert extract_city("123 Main St, Los Angeles, CA 90001") == "Los Angeles"


def test_extract_state():
    """Verify that extract_state correctly isolates the 2-letter state abbreviation."""
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("1600 Pennsylvania Ave NW, Washington, DC 20500") == "DC"
    assert extract_state("123 Main St, Los Angeles, CA 90001") == "CA"


def test_extract_zipcode():
    """Verify that extract_zipcode correctly isolates the 5-digit postal code."""
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("1600 Pennsylvania Ave NW, Washington, DC 20500") == "20500"
    assert extract_zipcode("123 Main St, Los Angeles, CA 90001") == "90001"
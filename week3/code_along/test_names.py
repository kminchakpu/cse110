from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Test the make_full_name function with various name formats."""
    # This will FAIL first because of the missing space bug!
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Al", "Li") == "Li; Al"
    assert make_full_name("Martha", "Smith-Washington") == "Smith-Washington; Martha"

def test_extract_family_name():
    """Test that extract_family_name correctly isolates the family name."""
    # This one should pass right away
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Li; Al") == "Li"
    assert extract_family_name("Smith-Washington; Martha") == "Smith-Washington"

def test_extract_given_name():
    """Test that extract_given_name correctly isolates the given name."""
    # This will CRASH/FAIL first because of the "/ " bug!
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Li; Al") == "Al"
    assert extract_given_name("Smith-Washington; Martha") == "Martha"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
import pytest
from template_library.my_module import Processor, get_current_capacity_info
from template_library.other_module import DEFAULT_CAPACITY


# --- Tests for my_module ---

def test_processor_initial_state():
    """Test Processor initializes with correct default load and capacity."""
    processor = Processor()
    # Check current load (should be 0) and capacity (from other_module)
    assert processor.current_load == 0
    assert processor.max_capacity == DEFAULT_CAPACITY


def test_processor_add_valid_load():
    """Test adding load successfully."""
    processor = Processor()
    assert processor.add_load(50) is True
    assert processor.current_load == 50


def test_processor_add_load_over_capacity():
    """Test adding load that exceeds the maximum capacity."""
    processor = Processor()
    processor.current_load = 50
    # Try to add 51 (total 101, max 100)
    assert processor.add_load(51) is False
    # Ensure load remains unchanged
    assert processor.current_load == 50


def test_processor_add_negative_load_raises_value_error():
    """Test exception handling for negative input."""
    processor = Processor()
    with pytest.raises(ValueError):
        processor.add_load(-10)


def test_get_current_capacity_info_contains_value():
    """Test the capacity info function returns the expected text."""
    info = get_current_capacity_info()
    expected_substring = f"Global maximum capacity is set to {DEFAULT_CAPACITY} units."
    assert expected_substring in info

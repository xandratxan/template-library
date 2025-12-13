from template_library.other_module import UtilityManager, generate_id


# --- Tests for other_module ---

def test_utility_manager_default_multiplier():
    """Test UtilityManager initialization with default multiplier."""
    manager = UtilityManager()
    assert manager.multiplier == 1.0


def test_utility_manager_custom_multiplier():
    """Test UtilityManager initialization with a custom multiplier."""
    manager = UtilityManager(multiplier=2.5)
    assert manager.multiplier == 2.5


def test_utility_manager_apply_factor():
    """Test the calculation performed by apply_factor."""
    manager = UtilityManager(multiplier=10.0)
    assert manager.apply_factor(5.0) == 50.0
    assert manager.apply_factor(0.5) == 5.0


def test_generate_id_structure():
    """Test that the generated ID starts with the correct prefix."""
    prefix = "TEST"
    id_string = generate_id(prefix)
    assert id_string.startswith(prefix)
    assert '-' in id_string

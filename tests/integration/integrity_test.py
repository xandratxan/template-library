# Import objects from both modules
from template_library.my_module import Processor
from template_library.other_module import DEFAULT_CAPACITY


def test_processor_max_capacity_is_linked_to_other_module_constant():
    """
    Verify that Processor.max_capacity inherits the value from
    other_module.DEFAULT_CAPACITY.
    """
    processor = Processor()

    # Check initialization value
    assert processor.max_capacity == DEFAULT_CAPACITY

    # Use the capacity value to test boundary conditions
    # Adding exactly the max capacity (100) when load is 0 should succeed
    processor.current_load = 0
    assert processor.add_load(DEFAULT_CAPACITY) is True

    # Adding one more than the max capacity (101) when load is 0 should fail
    processor_fail = Processor()
    assert processor_fail.add_load(DEFAULT_CAPACITY + 1) is False

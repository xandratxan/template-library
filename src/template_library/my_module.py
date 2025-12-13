"""
my_module.py
------------
Contains the core processing class that depends on other_module.
"""

# Dependency: Import a constant from the sibling module
from .other_module import DEFAULT_CAPACITY


class Processor:
    """
    The main data processing class for the template library.

    It uses the `DEFAULT_CAPACITY` constant from `other_module`
    to set its internal limit.

    Attributes
    ----------
    max_capacity : int
        The maximum allowed load, inherited from :const:`other_module.DEFAULT_CAPACITY`.
    current_load : int
        The current processing load (starts at 0).
    """

    def __init__(self):
        """
        Initializes the processor using the default capacity from other_module.
        """
        self.max_capacity = DEFAULT_CAPACITY  # Dependency used here
        self.current_load = 0

    def add_load(self, amount: int) -> bool:
        """
        Increases the processing load.

        Parameters
        ----------
        amount : int
            The integer amount to add to the current load.

        Returns
        -------
        bool
            True if load was added successfully, False otherwise.

        Raises
        ------
        ValueError
            If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Load amount cannot be negative.")

        if self.current_load + amount <= self.max_capacity:
            self.current_load += amount
            return True
        return False


def get_current_capacity_info() -> str:
    """
    Retrieves the global maximum capacity as defined in other_module.

    Returns
    -------
    str
        A string summarizing the current capacity setting.
    """
    # Dependency used here
    return f"Global maximum capacity is set to {DEFAULT_CAPACITY} units."

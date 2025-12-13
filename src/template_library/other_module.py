"""
other_module.py
---------------
Contains a configuration constant and a utility class.
"""

# Global Constant used for configuration across the library
DEFAULT_CAPACITY: int = 100
"""
The default maximum capacity for processing units in the library.
"""


class UtilityManager:
    """
    A simple manager class providing utility methods.

    This class is often used internally by primary classes in the library.

    Attributes
    ----------
    multiplier : float
        A factor to apply in subsequent calculations.
    """

    def __init__(self, multiplier: float = 1.0):
        """
        Initializes the Utility Manager.

        Parameters
        ----------
        multiplier : float, optional
            A factor to apply in calculations (default is 1.0).
        """
        self.multiplier = multiplier

    def apply_factor(self, value: float) -> float:
        """
        Applies the internal multiplier to an input value.

        Parameters
        ----------
        value : float
            The input number.

        Returns
        -------
        float
            The multiplied result.
        """
        return value * self.multiplier


def generate_id(prefix: str) -> str:
    """
    Generates a unique identifier string.

    Parameters
    ----------
    prefix : str
        The string prefix for the ID.

    Returns
    -------
    str
        A unique identifier string based on the prefix.
    """
    import time
    return f"{prefix}-{int(time.time() * 1000)}"

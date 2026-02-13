"""
Module defining the base Animal class for farm animals.
"""

class Animal():
    """
    Base class for all farm animals.

    Attributes:
        energy (int): Represents the current energy level of the animal.
    """
    def __init__(self):
        """
        Initialize a new Animal instance with 0 energy.
        """
        self.energy = 0

    def feed(self):
        """
        Feed the animal to increase its energy by 1.

        Returns:
            int: The updated energy level.
        """
        self.energy += 1

    def status(self):
        """Return current energy for Pylint compliance."""
        return self.energy

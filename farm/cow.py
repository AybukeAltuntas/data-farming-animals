"""
Module defining the Cow class, inheriting from Animal.
"""

from farm.animal import Animal

class Cow(Animal):
    """
    Represents a cow on the farm, inheriting from Animal.

    Attributes:
        milk (int): Amount of milk produced by the cow.
        energy (int): Inherited from Animal; represents the cow's energy level.
    """
    def __init__(self):
        """
        Initialize a new Cow instance with 0 milk and inherited energy.
        """
        super().__init__()
        self.milk = 0

    def talk(self):
        """
        Make the cow 'speak'.

        Returns:
            str: The sound the cow makes ('moo').
        """
        return 'moo'

    def feed(self):
        """
        Feed the cow to increase its energy and milk production.

        Increases:
            energy by 1
            milk by 2

        Returns:
            tuple: A tuple containing (energy, milk)
        """
        super().feed()
        self.milk = self.milk + 2
        return self.energy, self.milk

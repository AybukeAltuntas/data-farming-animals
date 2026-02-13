"""
Module defining the Chicken class, inheriting from Animal.
"""

from farm.animal import Animal


class Chicken(Animal):
    """
    Represents a chicken on the farm, inheriting from Animal.

    Attributes:
        gender (str): 'male' or 'female'
        eggs (int): Number of eggs produced by the chicken
        energy (int): Inherited from Animal; represents the chicken's energy level
    """
    def __init__(self,gender):
        """
        Initialize a new Chicken instance with specified gender, 0 eggs, and inherited energy.

        Args:
            gender (str): 'male' or 'female'
        """
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        """
        Make the chicken 'speak' based on its gender.

        Returns:
            str: 'cluck cluck' if female, 'cock-a-doodle-doo' if male
        """
        if self.gender == 'female':
            return 'cluck cluck'
        return 'cock-a-doodle-doo'

    def feed(self):
        """
        Feed the chicken to increase its energy and, if female, egg production.

        Increases:
            energy by 1
            eggs by 2 (only if female)

        Returns:
            int or tuple:
                - For female: (energy, eggs)
                - For male: energy
        """
        super().feed()
        if self.gender == 'female':
            self.eggs = self.eggs + 2
            return self.energy, self.eggs

        return self.energy

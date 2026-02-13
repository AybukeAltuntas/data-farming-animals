from farm.animal import Animal

class Cow(Animal):

    def __init__(self):
        super().__init__()

    def talk(self):
        return 'moo'

    def feed(self):
        super().feed()

from abc import ABC,abstractmethod



class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def describe(self):
        print('That ia a general description of the animal')

class Dog(Animal):
    def make_sound(self):
        print('Sound: Dogs Bark')
    def describe(self):
        print('Description: Dogs are domesticated mammals known for their loyalty and diverse appearances.')
class Cat(Animal):
    def make_sound(self):
        print('Sound: Cats Meows')
    def describe(self):
        print('Description: Cats are known for their sleek bodies, sharp claws, and keen senses, particularly their excellent night vision and hearing.')
class Cow(Animal):
    def make_sound(self):
        print('Sound: Cows Moo')
    def describe(self):
        print('Description: Cows are large, domesticated, hoofed mammals with a robust body, broad head, and long legs.')






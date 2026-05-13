# Parent Class
class Toy:
    def make_sound(self):
        print("Whirrr!")

    def hello(self):
         print("Hello")

# Child Class inherits from Toy
class Car(Toy):
    def drive(self):
        print("Vroom!")

# Usage
my_car = Car()
toy = Toy()
my_car.make_sound()  # Output: Whirrr! (Inherited)
my_car.drive()    # Output: Vroom! (Specific to Car)
my_car.hello()

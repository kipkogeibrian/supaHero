class Superhero:
    """Base class for all superheroes"""
    
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.__power_level = power_level         # Private attribute
        
    def introduce(self):
        print(f"I am {self.name}! (Secret identity: {self._secret_identity})")
    
    def use_power(self):
        raise NotImplementedError("Subclasses must implement this!")
    
    @property
    def power_level(self):
        return self.__power_level
    
    @power_level.setter
    def power_level(self, value):
        if 0 <= value <= 100:
            self.__power_level = value
        else:
            print("Power level must be between 0-100!")

# Inheritance Example
class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, power_level, max_altitude):
        super().__init__(name, secret_identity, power_level)
        self.max_altitude = max_altitude
        
    def use_power(self):  # Polymorphism
        print(f"{self.name} soars {self.max_altitude} meters into the air!")
    
    def fly(self):        # Unique to FlyingHero
        print("Whoosh! ✈️")

# Create instances
superman = FlyingHero("Superman", "Clark Kent", 95, 2000)
superman.introduce()
superman.use_power()
superman.fly()
print(f"Power level: {superman.power_level}")

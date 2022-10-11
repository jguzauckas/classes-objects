# Pick one of the following concepts to build a class of (or choose your own!)
#   - Car (make, model, year, mileage, etc.)
#   - Smartphone (manufacturer, model, storage size, etc.)
#   - Shoes (brand, color, size, etc.)
#
# For your class, you should meet the following requirements:
#   - Have at least three attributes
#   - Have an __init__() and __str__() function
#   - Have at least one parameter with getter and setter methods
#   - Have two custom methods that do something with information
#   - One of your methods should have a parameter taken in
#
# With your completed class, effectively test it by:
#   - Creating two objects of that class
#   - Modifying a property of at least one object
#   - Print out the object to demonstrate the __str__() method
#   - Make at least one call to each of your methods


class Car:
    def __init__(self, make: str, model: str, year: int, mileage: float):
        self.make = make
        self.model = model
        self._year = year
        self.mileage = mileage

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        if value < 1700:
            print("This car does not exist!")
        else:
            self._year = value

    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model} ({self.mileage})"


class Smartphone:
    def __init__(self, manufacturer: str, model: str, storage_size: int) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self._storage_size = storage_size

    @property
    def storage_size(self) -> int:
        return self._storage_size

    @storage_size.setter
    def storage_size(self, value: int) -> None:
        if value <= 0:
            print("You need more storage space!")
        else:
            self._storage_size = value

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model} ({self.storage_size}GB)"


class Shoes:
    def __init__(self, brand: str, color: str, size: int) -> None:
        self.brand = brand
        self.color = color
        self._size = size

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        if value <= 0:
            print("Please enter a valid shoe size")
        else:
            self._size = value

    def __str__(self) -> str:
        return f"{self.brand} {self.color} Shoes ({self.size})"


c = Car("Honda", "Civic", 2005, 99999)
p = Smartphone("Apple", "iPhone 14 Pro Max", 128)
s = Shoes("Nike", "Red", 10.5)

print(c)
c.year = 2001
print(c)

print(p)
p.storage_size = 64
print(p)

print(s)
s.size = 12
print(s)

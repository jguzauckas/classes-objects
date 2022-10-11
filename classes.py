class MyClass:
    num = 10

obj = MyClass()

print(obj.num)

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

p1 = Person("Mr. G", 24)

print(f"{p1.name} is {p1.age} years old!")

print(p1)

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

p2 = Person("Mr. G", 24)
print(p2)

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    def hello(self) -> None:
        print(f"Hello {self.name}!")

p3 = Person("Mr. G", 24)
p3.hello()

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    @property
    def age(self) -> str:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        self._age = value

p4 = Person("Mr. G", 24)
p4.age = 25
print(p4.age)
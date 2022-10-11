# Object-Oriented Programming

Python is an object-oriented programming language, which means that when programming, we design things around groups of data, called **objects**.

In Python, we have a lot of built-in objects that we already have used, like `str` and our iterables: `tuple`, `list`, `set`, and `dict`. These are designed for us to use them as templates to hold our own information, like when we create any of these types of objects.

We call the framework a **class** and the actual times we use the class an **object**.

All of the sample code provided in this file is in the classes.py Python file for you to run, modify, and otherwise investigate.

---

## Classes

To program a framework, we use the keyword `class`. This syntax will look very similar to how we defined functions with `def`. Here is a very basic example of a class:

```python
class MyClass:
    num = 10
```

Following the class keyword, we give our class a name, and importantly, we distinguish classes from functions and variables by capitalizing the first letter of each word.

A framework is only so helpful though, until we start using to create objects in its image. After defining a class, we can create an object of its type using the class name as if it was a function:

```python
obj = MyClass()
```

Now the variable `obj` is an object of type `MyClass`. Now in our example, `MyClass` is very small and basic, so having an object is not that useful, but the object will contain all the features set out in the class. In this case, we have access to the variable `num` that was set to `10` inside of the class definition. We can access `num` using the dot operator `.` with our object:

```python
print(obj.num)
```

This produces the output:

```
10
```

---

## Other Class Methods

While there are a couple of standard functions like we've gone over, one of the most powerful parts of making classes is the ability to write functions that are more customized to your uses. We can make custom functions specifically for our classes, which we call **methods**.

Let's expand our `Person` class one more time to add another method:

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    def hello(self) -> None:
        print(f"Hello {self.name}!")
```

The only thing that has changed from our previous `Person` class is two more lines, adding in the method `hello()`. Continuing the trend from our first two standard functions, we have to include the `self` parameter to utilize any information stored by the object. We also note the `None` return type hint as we just intend to print the information when the method is called.

To utilize this method, we use the dot operator `.` with our object to call this like we would any other function. We also don't need parameters, since Python handles the `self` parameter on its own:

```python
p3 = Person("Mr. G", 24)
p3.hello()
```

This produces the output:

```
Hello Mr. G!
```

---

## Attributes and Properties

So far we've made classes that have **attributes**, which are assigned at creation. Often we want more dynamic and specific control of our information though, and to do that, we expand on our attributes to make them **properties**.

Oftentimes, we want specific control over two interactions with our information, in the form of **getters** and **setters**. Getters are functions that allow us to _get_ the value of a property, and setters are functions that allow us to _set_ the value of a property. Python has a way for us to do this a little more quickly than normal using the decorator `@`.

We'll do another expansion of our `Person` class, with getter and setter methods for the `age` property. We'll leave `name` as an attribute:

```python
class Person:
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
```

Note first that when using `self` with the dot operator `.` and our variable `age`, we now have slightly different syntax. The underscore `_` essentially marks our attribute as private, which is needed to be a property.

Our `@` decorators tell Python to treat our new methods as getters and setters. The simple decorator `@property` is for getters, so the method that comes after it should be treated as a getter method for its variable. The setter decorator uses the dot operator `.` and the variable name to make clear what the following method is a setter method for.

Note the return types on the getter and setter methods. Getters return the value, so they have a return type, and setters just set it, so they have a return type of `None`.

With those methods defined, we can easily get and set our property as a variable from outside of the class using the dot operator `.`:

```python
p4 = Person("Mr. G", 24)
p4.age = 25
print(p4.age)
```

This produces the output:

```
25
```

Note that even though in the class definition we had to use `_age`, when we are working with objects of the class we can just use `age`, which is one of the advantages of setting up these property methods.

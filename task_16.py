# Написать классы Animal, Dog, Cat, используя наследование,
# определить в них методы say(), ,whoami(), __init__()
# При вызове say() объекты Dog должны возвращать “bark”, объекты Cat - “meow”
# При вызове whoami() объекты Dog должны возвращать “Good Boy {name}”
# объекты Cat - “Arrogant Creature {name}”, Animal - “Unknown Beast”
# Если это для вас слишком просто можете пофлексить и придумать свои сценарии,
# например Person Employee Developer SysAdmin с разными методами, вроде calculate_salary()

class Animal:
    def __init__(self, name):
        self.name = name

    def say(self):
        return self.name

    def whoami(self):
        return f"Unknown Beast"


class Dog(Animal):
    def say(self):
        return "bark"

    def whoami(self):
        return f"Good Boy {self.name}"


class Cat(Animal):
    def say(self):
        return "meow"

    def whoami(self):
        return f"Arrogant Creature {self.name}"


animal = Animal("Beast")
print(animal.say())
dog = Dog("Gory")
print(dog.whoami())
print(dog.say())
cat = Cat("Murka")
print(dog.say())
print(cat.say())
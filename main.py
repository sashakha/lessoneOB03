class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic sound")

    def eat(self):
        print(f"{self.name} ест")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("ГАВ!")

    def play(self):
        print(f"{self.name} играет")


dog = Dog("Шарик", 5)
dog.make_sound()
dog.eat()
dog.play()


class Bird(Animal):
    def make_sound(self):
        print("Чирик!")


class Cat(Animal):
    def make_sound(self):
        print("Мурлык!")


class Reptile(Animal):
    def make_sound(self):
        print("Шшш!")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Создание объектов разных классов
bird = Bird("Чижик", 1)
cat = Cat("Кошка", 3)
reptile = Reptile("Ящерица", 2)

animals = [bird, cat, reptile]

animal_sound(animals)


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, {type(animal).__name__}")

    def list_employees(self):
        for employee in self.employees:
            print(f"{employee.name}, {type(employee).__name__}")


class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animals(self, animals):
        print(f"{self.name} is feeding the animals.")
        for animal in animals:
            animal.eat()


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name} the {type(animal).__name__}.")


# импорт в список
import json


class Zoo:

    def save_to_file(self, filename):
        data = {
            "animals": [{"name": animal.name, "age": animal.age, "type": type(animal).__name__} for animal in
                        self.animals],
            "employees": [{"name": employee.name, "type": type(employee).__name__} for employee in self.employees]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.animals = []  # Очистить текущий список
            self.employees = []  # Очистить текущий список





import re
import random



# Education create Classes and Objects
class Student():
    def __init__(self, name, id, Kuzya = 0):
        self.name = name
        self.id = id
        self.Kuzya = Kuzya
    def changeID(self, id):
        self.id = id
    def Kuzyafication(self):
        self.Kuzya = self.name + 'Kuzya'
    def print(self):
        print("{}-{}-{}".format(self.name, self.id, self.Kuzya))

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        area = self.width * self.height
        print("Area: {}".format(area))


# Privat, public attribute. Encapsulation
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._id = random.randint(0, 1000)
    def print(self):
        print("{}-{}-{}".format(self.username, self.password, self._id))

    #def main():
    #user = User("Denis", "123")
    #user.password = "111"
    #user._id = 111
    #user.print()

 # Наследование (Inheritance)
""" class Person():
        def __init__(self, firstname, lastname, age):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            if age < 0:
                self.age = 0
        def print(self):
            print("{}-{}-{}".format(self.firstname, self.lastname, self.age))

class Employee(Person):
    def __init__(self, firstname, lastname, age, inn, number, snils):
        Person.__init__(self, firstname, lastname, age)
        self.inn = inn
        self.number = number
        self.snils = snils
    def print(self):
        print("{}-{}-{}-{}-{}-{}".format(self.firstname, self.lastname, self.age, self.inn, self.number, self.snils)) """

#def main():
    #employee = Employee("Denis", "Bezv", -18, "59022588432", "12356548", "458-586")
    #employee.print()


# Полиморфизм (Polymorphism)
class Person():
        def __init__(self, firstname, lastname, age):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            if age < 0:
                self.age = 0
        def print(self):
            print("{}-{}-{}".format(self.firstname, self.lastname, self.age))
        def greeting(self):
            print("Привет, я человек и меня зовут {}".format(self.firstname))

class Employee(Person):
    def __init__(self, firstname, lastname, age, inn, number, snils):
        Person.__init__(self, firstname, lastname, age)
        self.inn = inn
        self.number = number
        self.snils = snils
    def print(self):
        print("{}-{}-{}-{}-{}-{}".format(self.firstname, self.lastname, self.age, self.inn, self.number, self.snils))
    # Переопределение метода
    def greeting(self):
            # print("Привет, я работник и меня зовут {}".format(self.firstname))
#def main():
    #employee = Employee("Denis", "Bezv", -18, "59022588432", "12356548", "458-586")
    #person = Person("Kuzya", "Bezv", 5)
    #employee.greeting()
    #person.greeting()


# Агрегация и композиция




if __name__ == "__main__":
    main()



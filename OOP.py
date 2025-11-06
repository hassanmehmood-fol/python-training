class Car3:
    color = "Black"
    model = "2024"


car1 = Car3()
print(car1.color)


class Car1:
    def start(self):
        print("Car started")


c = Car1()
print(type(c))
c.start()


# class Dog:
#   def __init__(self,sound):
#     self.sound=sound
#   def sound_info(self):
#      print(f'The dog sound is ',self.sound)


# c1=Dog('bow_bow')
# c1.sound_info()


class Car3:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def info(self):
        print(f"Company: {self.company}, Model: {self.model}")


c1 = Car3(company="Civic", model="Ho  nda ")
c1.info()


class Student:
    def __init__(self, name1):
        self.name = name1

    def show(self):
        print("Student name is:", self.name)


s1 = Student("Hassan")
s1.show()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")


dog1 = Dog("Buddy", "Woof Woof")
dog1.speak()

#inheritance
#passing parent class as an argument to the definition of clild

class Animal:
  def make_sound(self, sound):
    print(sound)

  cool = True

class Cat(Animal):
  pass

gandalf = Cat()
gandalf.make_sound('meow')
gandalf.cool

#isinstance
print(isinstance(gandalf, Animal))

#Properties

class Human:
  def __init__(self,first,last,age):
    self.first = first
    self.last = last
    if (age >= 0):
      self._age = age
    else:
      self._age = age
  @property
  def age(self):
    return self._age
  @age.setter
  def age(self, value):
    self._age = value

  @property
  def full_name(self):
    return f'{self.first} {self.last}'

  full_name.setter
  def  full_name(self, name):
    self.first, self.last = name.split(" ")

jane = Human('Jane', 'Goodall', -9)
print(jane.age)
jane.age = 20
print(jane.age)
jane.full_name ="Bizhan Gholikhamseh"
print(jane.full_name)
print(jane.__dict__)




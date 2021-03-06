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

class User:
  active_users = 0
  @classmethod
  def display_active_users(cls):
    print(cls)
  @classmethod
  def from_string(cls, data_str):
    first,last,age = data_str.split(',')
    return cls(first,last,int(age))
    #cls(data_str.split(','))
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age
    User.active_users +=1
  def __repr__(self):
    return f'{self.first} is {self.age}'
  def logout(self):
    User.active_users -= 1
    return f'{self.first} has logged out'
  def full_name(self):
    User.active_users -= 1
    return f'{self.first} {self.last}'

  def initials(self):
    return f'{self.first[0]} {self.last[0]}'
  def is_senior(self):
    return self.age >= 65
  def birthday(self):
    self.age += 1
    return f'Happy {self.age}th, {self.first}'

class Moderator(User):
  def __init__(self, first,last,age, community):
    super().__init__(first,last,age)
    self.community = community
  def remove_post(self):
    return f'{self.full_name()} removed a post from {self.community} community'

jasmine = Moderator('Jasmine', 'O Conner', 30, 'Piano')

print(jasmine.community)
  



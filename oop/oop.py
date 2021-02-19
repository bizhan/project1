#naming conventions
# _name. private member
#  __name  : name mangling. Make this variable particular to
#  To the class that it defines it.

#Class Attributes
#defines only once and shared by all instances of a class and
#class itself
class User:
  active_users = 0
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age
    User.active_users +=1

class Pet:
  allowed = ['cat','dog','fish','rat']
  def __init__(self, name, species):
    if species not in Pet.allowed:
      raise ValueError(f"You can not have a {species}")
    self.name = name
    self.species = species

cat = Pet('Blue', 'cat')
dog = Pet('Wyatt', 'dog')
Pet.allowed.append("pig")
pig = Pet('jake', 'pig')

#id python assigned unique number
print(id(cat.allowed))
print(id(dog.allowed))
print(id(pig.allowed))
print(id(Pet.allowed))

#Class Methods
# @classmethod decorator

class Userr:
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
    Userr.active_users +=1

print(Userr.display_active_users)
bizhan = Userr.from_string("Bizhan,Gholikhamseh,62")


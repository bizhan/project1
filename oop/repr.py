#__repr__ : provide nicer string represntation
#__str__ and __format__ doing the same.

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
  def __repr__(self):
    return f'{self.first} is {self.age}'

print(Userr.display_active_users)
bizhan = Userr.from_string("Bizhan,Gholikhamseh,62")
print(bizhan)
biz = Userr("judy",'steele',19)
biz = str(biz)
print(biz)
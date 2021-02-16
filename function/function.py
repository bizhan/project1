def exponent (num = 2, power=2):
  return num ** power

print(exponent(2,3))
print(exponent(2))
print(exponent(7))
print(exponent(power=8))

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

#example of setting default argument
def math(a, b, fn=add):
  return fn(a,b)


print(math(5,3))
print(math(5,3,fn=subtract))

def speak(animal='dog'):
  noises ={'dog': 'bark', 'cat': 'meow'}
  return noises.get(animal, '?')

def full_name(first, last):
  return "Your name is {} {}".format(first,last)

print(full_name('bizhan', 'gholikhamseh'))
#example of making keyword argument
print(full_name(last= 'gholikhamseh', first='bizhan'))



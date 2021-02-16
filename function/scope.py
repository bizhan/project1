#global variable
instructor ='Colt'
def say_hello():
  return f'Hello {instructor}'
print(say_hello())

total = 0
def increment():
  global total #now the total value could be manipulated
  total += 1
  return total

print(increment())

#nonlocal;
# modify a parent's variable in a child function
def outer():
  count = 5
  def inner():
    nonlocal count
    count += 1
    print(count)
    return count
  return inner()

print(outer())
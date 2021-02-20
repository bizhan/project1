#Generators are iterators
#Generators can be created with generator functions
#Generator function use the yield keyword
#Generators can be created with generator expressions

#Generator functions:
# return yield instead of return
# can yield multiple times
# when invoked, returns a generator

def count_up_to(max):
  count = 1
  while count <= max:
    yield count
    count +=1

gen = count_up_to(10)
while True:
  num = next(gen)
  print(num)
  if num == 10:
    break

print(list(count_up_to(10)))

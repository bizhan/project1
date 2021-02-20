#iterator is not the samething as iterable
#iter and next
#build loop
#generators
#compare generators functions and generator expressions
#use generators to pause execution of expensive functions

#iterator: an object can be iterated upon. an object that
# returns data, one element at a time when next() is called.

#iterable; an object which will return an iterator when. iter() is called on it.

# "HELLO" is an iterable, but it is not an iterator.
# iter("HELLO") returns an iterator

#next() is called on an iterator, the iterator returns
# the next item. It keeps doing so until it raises an
# Stopiteration error.

#custom for loop
it =  iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))
#print(next(it))

def my_for(iterable, func):
  it = iter(iterable)
  while True:
    try:
      thing = next(it)
    except StopIteration:
      break
    else:
      func(thing)

#my_for([1,2,3,4,5,6,7,8])
#my_for('HELLO')
my_for({'name': 'bizhan', 'last': 'jaffar'},print)

class Counter:
  def __init__(self, low, high, increment=1):
    self.current = low
    self.high = high
    self.increment = increment
  def __iter__(self):
    return self
  def __next__(self):
    if self.current + self.increment <= self.high:
      num = self.current
      self.current += self.increment
      return num
    raise StopIteration


for i in Counter(0,5,2):
  print(i)    

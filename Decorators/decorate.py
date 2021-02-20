#higher order functions can return functions from inside
# or accept a function as parameter.

from random import choice
def sum(n, func):
  total = 0
  for i in range(n):
    total += func(i)
  return total

def greet(person):
  def get_mood():
    msg = choice(('Hello there', 'Go away', 'I love you '))
    return msg

  result = get_mood() + person
  return result

def make_laugh_at_func(person):
  def get_laugh():
    laugh = choice(('HAHAHA','lol','tehehe'))
    return f'{laugh} {person}'
  return get_laugh  

laugh_at = make_laugh_at_func("Linda")
print(laugh_at())

#decorators
#are functions, wrap other functions and enhance behavior
#examples of higher order functions
# @

def be_polite(fn):
  def wrapper():
    print("What a pleasure to meet you!")
    fn()
    print("Have a great day!")
  return wrapper

def greet():
  print("My name is Colt.")

greet = be_polite(greet)
greet()

@be_polite
def rage():
  print("I Hate you")

rage()

#decorators with different signature
def shout(fn):
  def wrapper(*args, **kwargs):
    return fn(*args, **kwargs).upper()
  return wrapper

@shout
def greet(name):
  return f'HI, I am {name}'

@shout
def order(main, side):
  return f'HI, I would  like the {main}, with a. side of {side}' 
print(greet('Bizhan'))
print(order(side='burger', main='fries'))

def my_decorator(fn):
  def wrapper(*args, **kwargs):
    #do some stuff with fn(*args, **kwargs)
    pass
  return wrapper

#Preserving Metadata
# wraps: is a functool that wraps preserves function metadata
from functools import wraps
def log_function_data(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    print(f'you are about to call {fn.__name__}')
    print(f"Here's the documentation: {fn.__doc__}")
    return fn(*args, **kwargs)
  return wrapper

@log_function_data
def add(x,y):
  '''Adds two numbers together. '''
  return x + y;
print(add(3,6))
help(add)

from time import time
def speed_test(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    start_time = time()
    result = fn(*args, **kwargs)
    end_time = time()
    print(f"Time elapsed: {end_time - startime}")
    return result
  return wrapper

help(sum)
#### THIS DOESNOT WORK
#@speed_test
#def sum_nums():
#  return sum( x for x in range(1000000))
#print(sum_nums())

def ensure_no_kwargs(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    if kwargs:
      raise ValueError('No kwargs allowed! sorry : ')
    return fn(*args, **kwargs)
  return wrapper


@ensure_no_kwargs
def greet(name):
  print(f"Hi there {name}")
greet("Bizhan")

#greet('name=bizhan') THis will fail.

#decorators taking arguments
def ensure_first_arg_is(val):
  def inner(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      if args and args[0] != val:
        return f"first arg needs to be {val}"
      return fn(*args, **kwargs)
    return wrapper
  return inner
@ensure_first_arg_is("burrito")
def fav_food(*foods):
  print(foods)

print(fav_food("burrito","ice_cream"))
print(fav_food("burrito1","ice_cream"))

#Forcing types with decorators

def enforce(*types):
  def decorator(f):
    def new_func(*args, **kwargs):
      #convert args into something mutable
      newargs = []
      for (a,t) in zip(args, types):
        newargs.append(t(a))
      return f(*newargs, **kwargs)
    return new_func
  return decorator

@enforce(str, int)
def repeat_msg(msg, times):
  for time in range(times):
    print(msg)
repeat_msg("hello", "3")





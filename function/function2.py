# *args gathers remaining arguments as a tuple
def sum_def(num1, num2, num3):
  return num1 + num2 + num

def sum_def_new(*args):
  print(args)
  total  =0
  for num in args:
    total += num
  return total

print(sum_def_new(10,10,10,20))

def ensure_correct_info(*args):
  print(args)
  if 'colt' in args and 'steele' in args:
    return 'Welcome back'
  else:
    return 'not welcomed'


print(ensure_correct_info('purple', 'colt', 'steele','colt steele'))


#**kwargs
# gather the remaining arguments as a dictionary

def fav_colors(**kwargs):
  print(kwargs)
  for key, value in kwargs.items():
    print(f"{key}:{value}")

print(fav_colors(colt="biz", ruby="ii"))

def special_greetings(**kargs):
  if 'david' in kargs:
    if kargs['david'] == 'brownsen':
      print("Best Actor")
  else:
    print("Who are you")

print(special_greetings(david='brownsen'))
print(special_greetings(julia='david'))

def combine_word(word, **kargs):
  print(kargs)
  if 'prefix' in kargs:
    print(word + kargs['prefix'])
  elif 'suffix' in kargs:
    print(kargs['suffix'] + word)
  else:
    print(word)


combine_word("child", suffix="man")

#parameter ordering
#1. parameter
#2. *args
#3. default parameter
#5. **kwargs
def diplay_info(a,b, *args, instructor='Colt', **kargs):
  return [a, b, args, instructor, kwargs]


#unpacking. *
#num[1,2,3,4,5]
#fun(*num)
#pass contents of the list (or tuple) indiviually to the fun

#unpacking dictionary **

#calculate
#iput : list of arguments
# make_float: boolean return  make_float
# operation: add, subtract, multiply, divide
# first number, second number message string that can be added

#def calculate(make_float=False, operation=add, message='The result ', first, second)
def add(a,b):
  return a + b
def subtract(a,b):
  return a - b
def multiply(a,b):
  return a * b
def divide(a,b):
  return a / b

def calculate1(first,second,operation, **args):
  print(args)
  if 'make_float' in args:
    if args['make_float']:
      a = float(first)
      b = float(second)
    else:
      a = int(first)
      b = int(second)
  result = operation(a,b)
  if 'message' in args:
    return args['message'] + str(result)
  else:
    return 'The result is: ' + str(result)

print(calculate1(3,5,add,make_float=True,message='And the result:'))


def calculate(**kwargs):
  operation = {
    'add': kwargs.get('first', 0) + kwargs.get('second', 0),
    'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
    'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
    'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
  }
  operation_value = operation[kwargs['operation']]
  is_float = kwargs['make_float']
  if is_float:
    return float(operation_value)
  else:
    return int(operation_value)

print(calculate(first=3,second=8,operation='add',make_float=False))


  

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

#documenting.  """ """
#random.randint.__doc__

#exercise: 
#write a fcn take a string and char, return how many time char is in string
def single_letter_count(str, chr):
  return tuple(str).count(chr)

print(single_letter_count('bizihan', 'i'))

print({'e': "helelo".count('e') for chr in "helelo"})
def multiple_letter_count(str, chr):
  return {chr: str.count(chr)}

print(multiple_letter_count('helleo', 'e'))

#palindrome

def is_palindrome1(str):
  # Find middle
  # If len of string is even: 0-7 (8): stop condition index till =<len/2
  # e.g. 0,7, 1,6,2,5,3,4. len = 8 len/2 4
  # if len of stirng is odd; till len?2
  # e.g 0,8, 1,7, 2,6, 3,5, till len/2
  length = len(str)
  hlen = int(length/2) 
  length -=1
  for i in range(0,hlen):
    print(f"{i} = {str[i]} = {str[length - i]}")
    if str[i] !=  str[length -i]:
      return False
  return True


def is_palindrome2(str):
  # Find middle
  # If len of string is even: 0-7 (8): stop condition index till =<len/2
  # e.g. 0,7, 1,6,2,5,3,4. len = 8 len/2 4
  # if len of stirng is odd; till len?2
  # e.g 0,8, 1,7, 2,6, 3,5, till len/2
  return str == str[::-1]

def is_palindrome(str):
  stripped = str.replace(" ","")
  return stripped == stripped[::-1]

print(is_palindrome('ab ccba'))

#frequency of finding a primitive
def frequency(lst,chr):
  return lst.count(chr)

print(frequency("biizhan",'i'))

#multiple even numbers
def mul_even_num(lst):
  num = [l for l in lst if l % 2 == 0]
  nu = 1
  for i in range(len(num)):
    nu *= num[i]
  return nu

print(mul_even_num([2,3,4,5,6]))

#capitalize
def capitalize(str):
  return str[0].upper() + str[1:]
print (capitalize("bizhan"))

#value is truthy if value
def compact(l):
  return [val for val in l if val]
print(compact([0,1,2,3,"",[],False,None, "all done"]))

#intersection
def interst(l1, l2):
  #return set(l1) & set(l2)
  return [val for val in l1 if val in l2]

print(interst([1,2,3], [2,5,7]))

#partition
def evalute(l):
  if l or l == 0:
    return True
  return False


def partition1(l, fn=evalute):
  truthy_list = []
  falsy_list = []
  for val in l:
    if val == 0:
      truthy_list.append(val)
      continue
    if fn(val):
      truthy_list.append(val)
    else:
      falsy_list.append(val)
  return [truthy_list, falsy_list]

def partition2(l, fn=evalute):
  truthy_list = []
  falsy_list = []
  return [[val for val in l if fn(val)], [val for val in l if not fn(val)]]

#This one does not work.
def partition(l, fn=evalute): 
  return [[l.pop(l.index(i)) for i in l if fn(i)],l]

print(partition([0,1,2,3,"",[],False,None, "all done"]))




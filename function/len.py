#len
#The argument could be sequence(string, tuple, list, range) 
# or collections (dictionary, set)
#For dictionary the number of key-value pairs.
print(len('hello'))
print('hello'.__len__())


#len is adator to call __len__

class Specialist:
  def __init__(self, data):
    self.__data = data

  def __len__(self):
    #return 50
    return self.__data.__len__() //2 # division by 2

l1 = Specialist([1,40,30,100])
print(len(l1))

#abs absolute value of a number
#import math. math.fabs(-4). 4

#sum
#it takes iterable and an optional start
#returns the sum of start and the items of an
# iterable from left to right and returns the total
print(sum([1,2,3],10))

#round
#return number rounded to ndigits precison after the
#decimal point. if ndigits is omitted or is None, it return
# the neerest interger to its input

print(round(1.212345,2))
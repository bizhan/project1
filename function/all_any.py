#all
#return. true if all elements of the iterable are
#truthy (or if the iteralbe is empty)
all([0,1,]) # False
all([char for char in 'eio' if char in 'aeiou'])
all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True
print(all([num % 2 == 0 for num in [2,4,6,18]]))
print(all([ num for num in [2,4,6,18] if num % 2 == 0]))
print(all([])) #True
#any
#return ture if any element of the iterable is truthy
# if the iterable is empty, return False

#generator expression: similiar to list
(name[0] == 'C' for name in ['Cat', 'Charley'])
#generator expression if all you doing is iterating once
#if you want to store and use generated results use list comprehession
#generators don't support indexing or slicing
#generators can't be added to lists

import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))
print('To do the same thing, it takes ...')
print(f'List comprehession: {list_comp} bytes')
print(f'Generator expression: {gen_exp} bytes')




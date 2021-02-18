#zip
#make an iterator that aggregates elements from each of the iterables
#returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
#The iterator stops when the shortest input iterable is exhausted.

print(list(zip([1,2,3],[4,5,6])))#[(1,4), (2,5) , (3.6)]
first_zip = zip([1,2,3],[4,5,6])
print(dict(first_zip))
words = ['hi', 'lol', 'haha', ':)']

five_by_two = [(0,1),(1,2),(2,3),(3,4),(4,5)]
print(list(zip(*five_by_two)))

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']
print(list(zip(students, midterms, finals)))
print([pair for pair in zip(midterms, finals)])
print({pair[0]:max(pair[1],pair[2]) for pair in zip(students,midterms, finals)})

print(dict(zip( students, map(lambda pair: max(pair), zip(midterms, finals)))))

str1 = 'hello'
str2 = 'world'
print((list(zip(str1,str2))))
output = list(zip(str1,str2))
print("".join(["".join(pair) for pair in output]))

nums = [1,4,6,8,11,12,13]
print([ x * 3 for x in list(filter(lambda x: x % 4 == 0, nums))])

def triple_and_filter(lst):
  return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

#extract_full_name
#accept a list of dictionaries, return new list of stings with 
names = [{'first': 'abbas', 'last': 'akbar'},
{'first':'James', 'last': 'bond'}]
print(["".join(word) for word in names])

def extract_full_name(l):
  return list(map(lambda val: '{} {}'.format(val['first'],val['last'],l)))
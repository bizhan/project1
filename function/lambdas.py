#add_values = lambda x, y : x+ y
#add_values(10,20)

#map
#takes two  arguments, a function and an iterable
#map objects could be iterated only once.
nums = [1,2,3,4,5]
doubles = map(lambda x: x*2, nums)
print(list(doubles))
print(list(doubles))#empty


people = ["Darcy",'christine','Dana','Annable']
print(list(map(lambda name: name.upper(), people)))

def decrement_list(lst):
  return list(map(lambda x: x -1 , lst))

print(decrement_list(nums))

#filter
#There is a lambda for each value in the iterable
#Returns filter object which can be converted into other iterables
#The object contains only the values that return true to the lambda

l = [1,2,3,4,5]
evens = list(filter(lambda x: x % 2 == 0 , l))# returns only True values
evens = list(map(lambda x: x % 2 == 0 , l))
print(evens)

names = ['austin','penny', 'anthony','angel','billy']
print(list(filter(lambda name: name[0] == 'a', names)))

users = [
  {"username": "samuel", 'tweets': ["hello"]},
  {"username": "katie", 'tweets': ["I love cat"]},
  {"username": "bob123", 'tweets': []},
  {"username": "doggo_luvr", 'tweets': ['dogs are best']},
  {"username": "guitar", 'tweets': []},
]
print(list(filter(lambda user: not user['tweets'] ,users)))

#combine map and filter
print(list(map(lambda u: u['username'].upper(),filter(lambda user: not user['tweets'] ,users))));


#list comprehension
#retuns a new list with 
#'Your instructor is ' + each value in the array,
#but only if the value is less than 5 characters

names = ['Lassie', 'Colt', 'Rusty']
[f"Your instructor is {name}" for name in names if len(name) <5]
list(map(lambda name: f"Your instructor is  {name}",
filter(lambda value: len(value) < 5, names)))

#all
#return True if all elements of 
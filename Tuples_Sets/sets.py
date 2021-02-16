#Formal mathematicaal sets
# No duplicate values (collection)
# Elements in sets are not ordered
# Can not access the items in sets by index.
# use in to find out an item is in set

s = set({1,2,3,4,5,6,7,8})
s1 = {1,2,3}
5 in s1 #False

#converting list to a set
cities = ['Los Angles', 'Florence', 'Boulder']
print(cities)
cities_set = set(cities)
print(cities_set)

#converting a set to a list
cities_list = list(cities_set)
print(cities_list)

#finding how many unique cities
print(len(set(cities_list)))

list_1 = [1,2,3,4,5,5]
print(list_1)
print(set(list_1))#{1, 2, 3, 4, 5}

#how many unique items in a list
list_2 ={1,1,1,2,3,3,3,5,6,7,7,7}
print(len(set(list_2))) #6 removing duplicates

#METHODS

#add
s = set([1,2,3])
s.add(5)

#remove
s.remove(5) #KeyError if items is not in the sets.

#discard
s.discard(5) #doesnot return if there is no item

#copy
another = s.copy()
another is s #False

#clear
another.clear()

#Set mathematics
# find union, intersection, symmetric_difference

math_students = {'Mathew', 'Helen', 'James', 'Aparna'}
biology_students = {'jane', 'Mathew', 'Charlotter', 'James', 'Mesut', 'Oliver'}
union_sets = math_students | biology_students 
print(union_sets)
intersection_sets = math_students & biology_students
print(intersection_sets)


#Problems
numbers = (1,2,3,4)
value = (1)
#convert list to tuple
values = [10,20,30]
values_tuple = tuple(values)
print(values_tuple)
#get a unique stuff
stuff = [1,3,1,5,2,5,1,5]
stuff_unique = set(stuff)
print(stuff_unique)

#Tuple: an odered collection or grouping of items
numbers = (1,2,3,4)
#immutable, unchangable
x = (1,2,3)
print(x[0])

alphabet = ('a', 'b', 'c', 'd')
#why use tuple:
# much faster than and safer than list
# used as valid keys in dictionary

#gets created with key word tuple also:
#first_tuple = ((1,2,3,3,3))
sec_tuple = tuple((5, 1, 2))
print(sec_tuple)

#use tuples as keys in dictionary
#use tuples as keys for any ordered data ...
locations = {
  (35.0, 39.69): "Tokyo Office",
  (40.71, 74.56): "New York Office",
  (37.77, 122.41): "San Francisco Office"
}
locations[(35.0, 39.69)] #"Tokyo Office"
locs = {(35.0, 39.69) : "Tokyo Office"}

#dictionary items return tuples
cat = {'name': 'biscuit', 'age': '0.5', 'fav_toy':'chapstick'}
print(cat.items()) #dict_items([('name', 'biscuit'), ('age', '0.5'), ('fav_toy', 'chapstick')])

#METHODS
#count
x = (1,2,3,3,3)
x.count(1) #1
x.count(3) #3

#index
t = (1,2,3,3,3)
t.index(1) #0
#t.index(5) # ValueError: 
t.index(3) # 2 only the first matching index is return

#nested tuples
num = (1,2,3,(4,5), 6, 7)
print(num.index((4,5))) #3


print('hello')
#clear
#empy out all the keys and values
dct = dict(hello = "bizhan")
print(dct)
dct.clear()
print(dct)

#copy
dct = dict(name = "bizhan", age = 62, height = 6, look = "great")
print(dct)
dct2 = dct.copy()
print(dct2)
print(dct is dct2) #different objects
print(dct2.clear())

#fromkeys
#calls on empty dict
#{}.fromkeys([list of keys], 'single value')
# the keys should be iteratable.
new_user = {}.fromkeys(['key1','key2','key3'],'value')
print(new_user)

#get
print(dct.get('name'))
print(dct.get('notexist')) #return None not an error

#examples;
bakery_stock = {
  'almond croissant' : 12,
  'toffee cookie' : 2,
  'tea cake' : 1
}
from random import choice
food = choice(['almond croissant','toffee cookie','tea cacke'])
if food in bakery_stock:
  print(f"{bakery_stock[food]} left")
else:
  print("No item is left")

quantity = bakery_stock.get(food)
if quantity:
  print("{} left".format(quantity))
else:
  print("No item is left")

#example 2
game_properties = ['current_sore','high_score','number_of_lives']
initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

#pop; remove item from dict
print(dct)
dct.pop('look')
print(dct)

#popitem: randomly remove dictionary elements
print(dct)
print(dct.popitem()) #returns tuple
print(dct)

#update: keys and values in a dictionary with another set of key value
first = dict(a = 1, b = 2, c = 3, d = 4, e = 5)
second = {}
second.update(first)
print(second)
print(second is first) #False
second['a'] = 'amazing'
print(second)
second.update(first) # update over writes.
print(second)
second.update({}) # does not change if passing empty dictionary
print(second)

#exercise
inventory = {'croissant': 19, 'bagel':4, 'muffin': 8, 'cake': 1}
stock_list = inventory.copy()
stock_list['cookie'] = 18
stock_list.pop('cake')
print(stock_list)




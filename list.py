#list the same as array
#list_name[" .."], '..']
#len of list: len(list_name)

# create an obj of range class
num = range(1,5)
# create a list from range obj.
list_num = list(num)
print(list_num)

#accesing values in a list
print(list_num[0])
print(list_num[-1])

#check value exist in a list
print(1 in list_num)

#accessing all values in a list
for num in list_num:
  print(num)

#accessing all vaalues in a list using while
i = 0
while i < len(list_num):
  print(list_num[i])
  i += 1

# f string example
colors = ["red", "blue", "green", "purple"]
idx = 0;
while idx < len(colors):
  print(f"{idx}: {colors[idx]}")
  idx += 1


#append
first_list = [1,2,3,4,5]
first_list.append(5)
print(first_list)

#extend
first_list.extend([6,7,8,9])
print(first_list)

#insert
first_list.insert(2, 'Hi!')
print(first_list)
first_list.insert(-1, 'Bye !')
print(first_list)

#pop
first_list.pop() # removes the last item in the list
first_list.pop(1) #removes the item index by 1.

#remove
#Remove the first item from the list whose value is x.
# Thows a ValueError if the item is not found.
# it does not return any value

#index: position of a item in the list
print(first_list)
print(first_list.index(8))
#find index after a position
first_list.append(8)
print(first_list.index(8, -1))
#start and end of index
print(first_list.index(5,5, 9))

#count: number of times x appears in the list
print(first_list.count(5))

#reverse: reverse the elements of the list (in-place)
count_list = [1,2,3,4,5]
print(count_list)
count_list.reverse()
print(count_list)

#sort: sort items of the list (in-place)
another_list = [5,2,1,4,8]
another_list.sort()
print(another_list)

#join: is a string method.
words = ['Coding', 'Is', 'Fun!']
' '.join(words) # Coding Is fun!
print(words)
print(' '.join(words))
name = ['Mr', 'Steele']
print('. '.join(name))

#clear
first_list.clear()
print(len(first_list))
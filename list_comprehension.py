#comprehension applies to other data strutures.
# create a new list ...
#syntax:
# [ __ for. __ in __ ]
#[<variable name> for <same variable> in < iteratable ob>]
nums = [1,2,3]
new_nums = [ x*10 for x in nums]
print(new_nums)

name = 'colt'
new_name = [char.upper() for char in name]
print(new_name)  #['C', 'O', 'L', 'T']

friends = ['ashley', 'matt', 'michael']
new_friends = [friend[0].upper() + friend[1:] for friend in friends]
print(new_friends) #['Ashley', 'Matt', 'Michael']

print([num * 10 for num in range(1,6)])#[10, 20, 30, 40, 50]
print([bool(val) for val in [0, [], '']]) #[False, False, False]

numbers = [1,2,3,4,5]
print([str(num) for num in numbers]) #['1', '2', '3', '4', '5']

#conditional list comprehension
print([num for num in numbers if num % 2 == 0]) #even
print([num for num in numbers if num % 2 != 0]) #odd

print([num * 2 if num % 2 == 0 else num/2 for num in numbers])

with_vowels = "This is so much fun!"
print([''.join(char for char in with_vowels if char not in "aeiou")])

list1 = ['Elie', 'Tim', 'Matt']
new_list1 = [char[0] for char in list1]
print(new_list1)

list2 = [1,2,3,4,5,6]
answer2 = [num for num in list2 if num % 2 == 0]
print(answer2)

list1 = [1,2,3,4]
list2 = [3,4,5,6]
print([l1 for l1 in list1 if l1 in list2]) #[3,4]

#First solution: if we want to lower only one character.
list1 = ["ELie", "TIm", "MAtt"]
list2 = [l1[::-1] for l1 in list1]
print([l2[:-1] + l2[-1].lower() for l2 in list2])

#second solution: works if we want to lower all the word
print([val[::-1].lower() for val in ['Elie', 'Tim', 'Matt']])

#For all the number between 1 & 100 (including 100)
# create a list that are divisable by 12
print([val for val in range(1,101) if val % 12 == 0])

#Fiven the string 'amazing' create a list containing all the letters
#from "amazing" but not vowels(a,e,i,o and u).
print([char for char in 'amazing' if char not in ['a','e','i','o','u']])
#Or use string not a list
print([char for char in 'amazing' if char not in 'aeiou'])






#slicing
#some_list[start:end:step]
first_list = [1,2,3,4,5]
first_list[1:] #[2,3,4,5]
first_list[3:] #[4,5]
first_list[-1:] #[5]
first_list[-3:] #[2,3,4,5]
second_list = first_list[0:] # make a copy of list
second_list is first_list # False
second_list == first_list # True
#index is exclusive counting
first_list[:2] # [1,2]
first_list[:5] #  [1,2,3,4,5]
first_list[1:3] # [2,3]
first_list[-1] # [1,2,3,4]
first_list[1:-1] # [2,3,4]
first_list = [1,2,3,4,5,6]
first_list[1::2] # [2,4,6]
first_list[::2] # [1,3,5]
first_lis[1::-1] # [2,1]
first_list[:1:-1] # [6,5,4,3] 
first_list[2::-1] # [3,2,1]

#Tricks
#reverse list/string
string = "This is fun!"
string[::-1]
#modify portions of lists
numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']

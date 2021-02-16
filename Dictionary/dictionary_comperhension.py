# {__:__ for __ in __}
# iterates over keys by default
# to iterate over keys and values using .items()

numbers = dict(first = 1, second = 2, third =3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)


num_dict = { num: num **2 for num in range(1,6)}
print(num_dict)

str1 = "ABC"
str2 = '123'
combo = {str1[l]: str2[l] for l in range(0, len(str1))}
print(combo)

instructor = {
  'name' : 'colt',
  'city' : 'san francisco',
  'color' : 'purple'
}
yelling_instructor = {k.upper(): v.upper() for k, v in instructor.items()}
yelling_instructor2 = {k[0].upper() + k[1:]: v.upper() for k, v in instructor.items()}
print(yelling_instructor2)

num_list = [1,2,3,4]
new_list2 = {num:('even' if num % 2 == 0 else "odd") for num in num_list}
print(new_list2)

keys = ['CA','NJ','RI']
values = ['California', 'New Jersey', 'Rhode Island']
dict1 = {keys[i] : values[i] for i in range(3)}
print(dict1)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
dict2 = {person[i][0] : person[i][1] for i in range(3)}
print(dict2)

#fromkeys can have an initial value as second parameter
#another form is dict.fromkeys('aeiou', 0)
dict3 = {}.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)
print(dict3)
dict4 = {char : 0 for char in 'aeiou'}

#chr(int) returns ascii representation.  <--
dict5 = {i: chr(i) for i in range(65, 91)}
print(dict5)

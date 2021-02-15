#lists con contain any kind of element, even other lists
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for l in nested_list:
  for v in l:
    print(v)

# Two ways of doing same thing as above.
[print(v) for v in l for l in nested_list ]
[[print(v) for v in l] for l in nested_list]

board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

new_list =[["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
print(new_list)

#[[0,1,2], [0,1,2], [0,1,2]]
num = [[l for l in range(3)] for k in range(3)]
print(num) #[[0, 1, 2], [0, 1, 2], [0, 1, 2]]

num = [l for l in range(3) for k in range(3)]
print(num) #[0, 0, 0, 1, 1, 1, 2, 2, 2]

num = [[l for l in range(10)] for k in range(10)]
print(num)

#list is for aany order data structure.
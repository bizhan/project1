#sorted
#returns. a new sorted list from the items in iterable
more_numbers = [6,1,8,2]
print(sorted(more_numbers))
#more_numbers.sort(). changes the more_numbers
#sorted(more_numbers) returns new sorted list

#can change direction of sorting
print(sorted(more_numbers))

#works on tuple but returns list
more_tuple = (6,1,8,2)
print(sorted(more_tuple, reverse=True))

users = [
  {"username": 'samuel', 'tweets':['I love me', 'I']},
  {"username": 'katie', 'tweets':['I love']},
  {"username": 'jeff', 'tweets':[], 'color': 'purple', 'num':10},
  {"username": 'bob123', 'tweets':[]},
  {"username": 'doggo_luvr', 'tweets':['dogy dog day']},
  {"username": 'guitar_gal', 'tweets':[]},
]

#print(sorted(users, key=len)) #sort based on num of key
print(sorted(users, key=lambda user: user['username'])) #sort based username

songs = [
  {'title': 'happy birthday', 'playcount':1},
  {'title': 'Survive', 'playcount':6},
  {'title': 'YMCA', 'playcount':99},
  {'title': 'Toxic', 'playcount':31},
]
print(sorted(songs, key=lambda u: u['playcount']))
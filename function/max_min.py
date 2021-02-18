#max
#return the largest item in an iterable or the
#the largest of two or more arguments
max([3,4,1,2]) #4
max((3,4,1,2)) #4
max('awesome') #'w'
max({1:'a', 3:'c', 2:'b'}) #3

names = ['Arya', 'Samson', 'Dora', 'Ollivander']
#shortest length
print(min(len(name) for name in names))
print(max(names, key= lambda n:len(n)))

songs = [
  {'title': 'happy birthday', 'playcount':1},
  {'title': 'Survive', 'playcount':6},
  {'title': 'YMCA', 'playcount':99},
  {'title': 'Toxic', 'playcount':31},
]
#max returns a dictionary in below statement
print(max(songs, key=lambda s: s['playcount'])['title'])

def extremes(lst):
  return (min(lst), max(lst))

print(extremes(names))

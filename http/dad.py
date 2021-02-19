
import  random

term = input("say something: ")
print(term)


rand_num = random.randint(0,5)
import requests
url = 'https://icanhazdadjoke.com/search'
response = requests.get(url, headers={'Accept' : 'application/json'},
params = {'term':'cat' , 'limit' : rand_num})
data = response.json()
print(data['results'])



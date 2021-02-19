#http
#DNS lookup
#HTTP request to a server
#server issues RESPONSE

#DNS server: name to ip address
#GET /. 200 ok from server
#
#HTTP Request headers
#Accept:  Acceptable content-types for response (html, json, xml)
#Cache-control: specify caching behavior
#User-Agent: Information about the software used to make the request

#HTTP Response headers
#Access-Control-Allow_origin: specify the domains that can make requests
#Allowed hTTP vervs that are allowed in request.

#status
#2xx success
#3xx redirect
#4xx client error
#5xx server error

#HTTP verbs

#GET can be cached can be bookmarked
#POsT 

#APIs
import requests
url = 'http://www.google.com'
#response = requests.get('https://news.ycombinator.com/')
#print(res.text)
response = requests.get(url)
print(f"{url} status {response.status_code}")

#response = requests.get( 'url', headers = {
#  'header1' : 'value1',
#  'header2' : 'value2'
#})

url = 'https://icanhazdadjoke.com/'
#response = requests.get(url, headers={'Accept': 'text/plain'})
response = requests.get(url, headers={'Accept': 'application/json'})
#print(response.text)
print(response.json())

#Quary; sending request with parameters
#http://www.example.com/?key1=value1&key2=value2
#OR 
#response = requests.get(url, 
#params={
#  'key1' = 'value1',
#  'key2' = 'value2'
#})

url = 'https://icanhazdadjoke.com/search'
response = requests.get(url, headers={'Accept' : 'application/json'},
params = {'term':'cat' , 'limit' : 1})
data = response.json()
print(data['results'])
#print(data['joke'])
#print(f'status {data["status"]}')
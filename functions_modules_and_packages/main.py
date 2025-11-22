# from calculator import add

# result = add(5, 3)
# print("The result is", result)

# from calculator import subtract
# result = subtract(5, 3)
# print("The result is", result)

# from calculator import multiply
# result = multiply(5, 3)
# print("The result is", result)

# from calculator import divide
# result = divide(5, 3)
# print("The result is", result)
import requests
import os

# r = requests.get('https://api.github.com/events')
r = requests.post('https://httpbin.org/post', data={'key': 'value'}, delay=5 , timeout=2)
# r = requests.put('https://httpbin.org/put', data = {'key':'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')
print(r.json() )


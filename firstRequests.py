# Why = Users need to be able to make requests in app!
import requests

# a text-bases response object
result1 = requests.get("http://127.0.0.1:8000/")
print("base result 1 print out === ", result1)

result1_text = result1.text
print(result1_text)

# a j-son base response object
result2 = requests.get("http://127.0.0.1:8000/jsonExample")
print("base result 2 print out === ", result2)

result2_json = result2.json()
print(result2_json)
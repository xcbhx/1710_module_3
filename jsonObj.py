# WHY = JSON objects allow efficent and uniform transportantion of data across the internet

import json

dictionary = {
    "key": "value"
}

# python dictionary syntax
dictionaryJoke = {
    "type": "success",
    "value": {
        "id": 493,
        "joke": "Chuck Norris can binary search unsorted data.",
        "categories": ["nerdy"]
    }
}

# dictionarySong = {
#     "type": "Pop Song",
#     "value": {
#         "title": "TRUSTFALL",
#         "artist": "Pink",
#         "album": "Trustfall",
#         "length": 214
#     }
# }

{
    "type": "success",
    "value": {
        "id": 493,
        "joke": "Chuck Norris can binary search unsorted data.",
        "categories": [
            "nerdy"
        ]
    }
}


with open('exampleObj.json', 'w') as outfile:
    json.dump(dictionaryJoke, outfile, indent=4)

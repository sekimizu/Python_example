# JavaScript Object Notation
import json

data = '''[
    {
        "name" : "Chuck",
        "phone" : {
            "type" : "intl",
            "number" : "1234567890"
        },
        "email" : {
            "hide" : "yes"
        }
    },
    {
        "name" : "Kenny",
        "phone" : {
            "type" : "string",
            "number" : "7777777777"
        },
        "email" : {
            "hide" : "no"
        }
    }
]'''

try:
    #info would be stored in dictionary format
    info = json.loads(data)
    print("Item count:", len(info))
    for item in info:
        print("Name", item["name"])
        print("Phone number", item["phone"]["number"])
except:
    print("JSON format error!!!")
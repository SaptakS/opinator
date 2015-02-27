import json
with open ("reviews.json", "r")  as fp:
    x = json.load(fp)
    for d in x:
        for review in d.values():
            for y in review:
                print y

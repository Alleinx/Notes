import json

x = [1, 'simple', 'list']

with open('test.txt', 'w') as f:
    json.dump(x, f)
    
with open('test.txt') as f:
    x = json.load(f)
    print(x, type(x))

    
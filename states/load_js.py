import json

chapter1 = [{"x": 293, "y": 379, "width": 211, "height": 43}]

# with open('chapter1.json','w') as f:
#     json.dump(chapter1,f)

def load_map(path):
    with open(path, 'r') as f:
        cp1 = json.load(f)
    return cp1




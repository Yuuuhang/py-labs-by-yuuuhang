
import json, sys, os


if os.path.exists('input.json'):
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
elif os.path.exists('data.json'):
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
else:

    data = json.loads(sys.stdin.read())


result = 0.0
for item in data:
    score = item.get('score', 0)
    weight = item.get('weight', 1)
    result += score * weight


print(round(result, 3))

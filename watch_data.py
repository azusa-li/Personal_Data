import json

user_name = 'cceatmore'

with open(f'query_results3/{user_name}.json', 'r') as f:
    data = json.load(f)

print(len(data))

for d in data:
    print(d['title'])
    step_str = d['steps']
    step_list = json.loads(step_str)
    print(json.dumps(step_list))
    break
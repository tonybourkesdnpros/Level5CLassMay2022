import json

result_raw = open('result.json', 'r')

result = json.load(result_raw)

version = result['result'][0]['version']

print(version)
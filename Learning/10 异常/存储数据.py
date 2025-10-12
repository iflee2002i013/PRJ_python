from pathlib import Path
import json

numbers = [2,5,4,6,7]

path = Path('number.json')
contents = json.dumps(numbers)
path.write_text(contents)

contents2 = path.read_text()
numbers2 = json.loads(contents2)

print(numbers2)
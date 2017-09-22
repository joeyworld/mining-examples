import json
from prettytable import PrettyTable

with open('result.json', 'r', encoding='utf8') as file:
    people = json.load(file)

friends_likes_count = [(person['name'], person['total_count']) for person in people]
friends_likes_count.sort(key=lambda x: x[1], reverse=True)

table = PrettyTable(field_names=['Name', 'Number of pages liked'])
[table.add_row(person) for person in friends_likes_count]
print(table)

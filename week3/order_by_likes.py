import json
from prettytable import PrettyTable

# 파일에서 데이터 가져오기
with open('result.json', 'r', encoding='utf8') as file:
    people = json.load(file)

# 1. 사람마다 좋아요 누른 페이지를 "좋아요 찍힌 순" 으로 정렬
# 2. 결과를 표로 그리기
for person in people:
    person_name = person['name']
    print('Table for {}'.format(person_name))
    person_likes = person['likes']
    person_likes.sort(key=lambda x: x['fan_count'], reverse=True)

    table = PrettyTable(field_names=['Page name', 'Likes'])
    for page in person_likes:
        table.add_row([page['name'], page['fan_count']])
    print(table)
    print()


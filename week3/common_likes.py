import json
from prettytable import PrettyTable

# 파일에서 읽어오기
people = json.load(open('result.json', 'r', encoding='utf8'))

# 사람 두 명의 순서쌍 조합하기
num_people = len(people)
combinations = [(people[person1], people[person2])
                for person1 in range(num_people) for person2 in range(person1 + 1, num_people)]

# 공통 좋아요 찾아서 표로 그리기
for combo in combinations:
    table = PrettyTable(field_names=['{}와 {}의 공통 좋아요'.format(combo[0]['name'], combo[1]['name'])])
    union = list(set(likes['name'] for likes in combo[0]['likes']) & set(likes['name'] for likes in combo[1]['likes']))
    for element in union:
        table.add_row((element, ))
    print(table)

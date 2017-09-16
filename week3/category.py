import json
from collections import Counter
from prettytable import PrettyTable

# 파일에서 읽어오기
with open('result.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)

# 페이지의 카테고리를 모아서 리스트에 담기
# 카운터를 활용하여 수 세기
categories = [like['category'] for person in data for like in person['likes']]
categories_count = Counter(categories)

# 이번에는 Top 30! 테이블로 그려보기
table = PrettyTable(field_names=['Category', 'Pages likes'])
for category in categories_count.most_common(30):
    table.add_row(category)
print(table)

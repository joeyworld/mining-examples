import json
from collections import Counter
from prettytable import PrettyTable

# JSON 파일 읽기
with open('result.json', 'r', encoding='utf8') as json_file:
    data = json.load(json_file)

# 모든 페이지 이름 & 좋아요 리스트로 담기, 그리고 카운터로 세기
all_pages = [page['name'] for person in data for page in person['likes']]
pages_count = Counter(all_pages)

# 테이블 그리기
table = PrettyTable(field_names=['페이지 이름', '좋아요 누른 친구 수'])
for kv in pages_count.most_common(20):
    table.add_row(kv)
table.align['페이지 이름'] = 'c'
table.align['좋아요 누른 친구 수'] = 'r'

print(table)

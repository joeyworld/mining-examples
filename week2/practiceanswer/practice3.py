import requests
import facebook
from prettytable import PrettyTable

# 연습문제 3 - "건국대학교" 키워드로 페이지 검색 후 좋아요 순으로 표 그리기

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
api = facebook.GraphAPI(access_token=ACCESS_TOKEN)

# 검색 쿼리 만들어서 검색하기
args = {
    'type': 'page',
    'q': '건국대학교',
    'fields': 'name, likes'
}
search_result = api.request('search', args)
data = search_result['data']

# Paging 활용하여 모든 검색 결과 수집하기
while True:
    try:
        search_result = requests.get(search_result['paging']['next']).json()
        data += (search_result['data'])
    except KeyError:
        break

# 좋아요 순으로 정렬
data = sorted(data, key=lambda x: x['likes'], reverse=True)
# 표로 그리기!
table = PrettyTable(field_names=['name', 'likes'])
for datum in data[:50]:
    table.add_row([datum['name'], datum['likes']])
print(table)

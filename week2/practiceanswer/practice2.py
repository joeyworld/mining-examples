import requests
from prettytable import PrettyTable

# 연습문제 2 - 코카콜라 vs 펩시

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
base_url = 'https://graph.facebook.com/v2.10/'
search_type = 'page'

# 코카 콜라의 좋아요 수는?
# 코카콜라 키워드로 페이지 검색
q = 'coca-cola'
result = requests.get('{}search?type={}&q={}&access_token={}'.format(base_url, search_type, q, ACCESS_TOKEN)).json()

# "코카콜라" 페이지는 당연히 첫번째로 뜨니깐, 해당 페이지의 id를 가져와서 검색
page_id = result['data'][0]['id']
fields = 'name, fan_count'
result = requests.get('{}{}?fields={}&access_token={}'.format(base_url, page_id, fields, ACCESS_TOKEN)).json()
coca_cola_likes = result['fan_count']
print('{}의 좋아요 수 : {}'.format(result['name'], result['fan_count']))

# 펩시의 좋아요 수는?
# 펩시 키워드로 페이지 검색
q = 'pepsi'
result = requests.get('{}search?type={}&q={}&access_token={}'.format(base_url, search_type, q, ACCESS_TOKEN)).json()

# 역시 이번에도 정확한 페이지는 당연히 첫번째로 뜨니깐, 해당 페이지의 id를 가져와서 검색
page_id = result['data'][0]['id']
fields = 'name, fan_count'
result = requests.get('{}{}?fields={}&access_token={}'.format(base_url, page_id, fields, ACCESS_TOKEN)).json()
pepsi_likes = result['fan_count']
print('{}의 좋아요 수 : {}'.format(result['name'], result['fan_count']))

# 한 술 더 떠서 표로 그려봅시다
table = PrettyTable(field_names=['Coke Type', 'likes'])
table.add_row(['Coca-cola', coca_cola_likes])
table.add_row(['Pepsi', pepsi_likes])
print(table)

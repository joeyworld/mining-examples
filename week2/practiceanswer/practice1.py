import facebook
import json
import requests

# 연습문제 1 - 내가 몇개의 페이지에 좋아요를 눌렀을까?

# SDK를 통하여 API 연결
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
api = facebook.GraphAPI(access_token=ACCESS_TOKEN)

# 나에 대한 정보 가져오기
me_object = api.get_object('me', fields='id, name, likes.fields(id, name, created_time, likes)')
my_likes = me_object['likes']

# Paging 이용하여 모든 좋아요 수집하기
while 'next' in my_likes['paging']:
    my_likes = requests.get(my_likes['paging']['next']).json()
    for datum in my_likes['data']:
        me_object['likes']['data'].append(datum)

# 딕셔너리로 말아서
data = {
    'name': me_object['name'],
    'likes': me_object['likes']['data'],
    'total_count': len(me_object['likes']['data'])
}

# JSON 에 저장!
with open('my_likes.json', 'w', encoding='utf8') as makefile:
    json.dump(data, makefile, ensure_ascii=False, indent=4)

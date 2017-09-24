import json
import requests

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
base_url = 'https://graph.facebook.com/v2.10/'
fields = 'name, likes.fields(name, category, fan_count), friends.fields(name, likes.fields(name, category, fan_count))'
result = requests.get('{}me?fields={}&access_token={}'.format(base_url, fields, ACCESS_TOKEN)).json()

# 최종 url 은 이런 식으로 나타납니다
# https://graph.facebook.com/v2.10/me?fields=name, likes.fields(name, category, fan_count), friends.fields(name, likes.fields(name, category, fan_count))&access_token=YOUR_ACCESS_TOKEN

# 맨 처음 요청을 파일로 저장해볼께요!
with open('response.json', 'w', encoding='utf8') as file:
    json.dump(result, file, ensure_ascii=False, indent=2)

# 나에 대한 좋아요 가져오기
my_likes = result['likes']
next_url = my_likes['paging']['next']
while True:
    try:
        next_result = requests.get(next_url).json()
        print(next_result)  # test
        my_likes['data'] += next_result['data']
        next_url = next_result['paging']['next']
    except KeyError:
        break

# 최종 데이터를 위한 자료구조
data = [
    {
        'name': result['name'],
        'likes': my_likes['data'],
        'total_count': len(my_likes['data'])
    }
]

# 친구들의 좋아요 가져오기
friends = result['friends']['data']
for friend in friends:
    try:
        friend_name = friend['name']
        friends_likes = friend['likes']
        friends_next_url = friends_likes['paging']['next']
        # test
        print('-------------------')
        print('name: {}'.format(friend_name))
    except KeyError:
        continue

    while True:
        try:
            next_result = requests.get(friends_next_url).json()
            print(next_result)  # test
            friends_likes['data'] += next_result['data']
            friends_next_url = next_result['paging']['next']
        except KeyError:
            friend_info = {
                'name': friend_name,
                'likes': friends_likes['data'],
                'total_count': len(friends_likes['data'])
            }
            data.append(friend_info)
            break

# 마지막에 JSON 파일로 저장하기
with open('result.json', 'w', encoding='utf8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

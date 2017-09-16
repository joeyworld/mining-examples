import json
import requests

ACCESS_TOKEN = 'EAACEdEose0cBAHreztuVnbeNCaatFMP2bhe4arZBsmF4Ii3idenhkXUqVBKxTV2dex3ocHAMi67TjY5XxDzpSj6SgZBZBqloKqxng1Ex0cEdRR89rWOtu1pD8NqdYKaFSZAJdzzZCN6Nmxcr5b8wPGu30eZBzZBXZC2kb9ZCWMckYhQhFkGfMlR0ibAkkViQY8O4ZD'
base_url = 'https://graph.facebook.com/'
fields = 'id, name, likes.fields(name,category), friends.fields(id, name, likes.fields(name, category))'
response = requests.get('{}me?fields={}&access_token={}'.format(base_url, fields, ACCESS_TOKEN)).json()

print(response)
# 나에 대한 좋아요 가져오기
my_likes = response['likes']
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
        'name': response['name'],
        'likes': my_likes['data']
    }
]

# 친구들의 좋아요 가져오기
friends = response['friends']['data']
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
                'likes': friends_likes['data']
            }
            data.append(friend_info)
            break

# 마지막에 JSON 파일로 저장하기
with open('result.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)

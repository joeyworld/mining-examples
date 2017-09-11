import json
import requests
import facebook

ACCESS_TOKEN = 'EAACEdEose0cBAG5Q4zcXofOAdJNlWHPP608G8eXxda1WPA38ZCnRB' \
               'K765ve5a7VpnzlviCQd05k9LG0JgFtkHgk8CJttwIpE23OLNDAzzB3Ima' \
               'NPz2fg1EmT8axuY9j4ZCv7qFdHPRu4jUiHu0YUKBkMmWKxLZC9zbxXfO0F' \
               'fB0YtVzqUdxBLYOnZBFnFt4ZD'
api = facebook.GraphAPI(access_token=ACCESS_TOKEN)

me_object = api.get_object('me', fields='id, name, likes')
my_likes = me_object['likes']
count = len(my_likes['data'])

while 'next' in my_likes['paging']:
    my_likes = requests.get(my_likes['paging']['next']).json()
    for datum in my_likes['data']:
        me_object['likes']['data'].append(datum)
    count += len(my_likes['data'])

del(me_object['likes']['paging'])
me_object['likes']['count'] = count

with open('my_likes.json', 'w', encoding='utf8') as makefile:
    json.dump(me_object, makefile, ensure_ascii=False, indent=4)

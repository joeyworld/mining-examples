import requests
import facebook
import json

ACCESS_TOKEN = 'EAACEdEose0cBALsX7DkHb5ZCmnVtHbtfyXuvCl2BpJwspHmHmEcce8mA5jJmqXWSMx9lawkLg2I4t3edurEPviOZAbpSsA7ZCLBQv6NkZCsQmpf33PXqpbmsK7ZBZC5KjJb3ZAvRx2bCn6EQfETy0FpDz5WZAWdXBiqRoObGLiVTbqUekJsMc6Q6hXA6O6QL97gZD'
api = facebook.GraphAPI(access_token=ACCESS_TOKEN)

me_object = api.get_object('me', fields='id, name, likes.fields(id, name, created_time, likes)')
my_likes = me_object['likes']

while 'next' in my_likes['paging']:
    my_likes = requests.get(my_likes['paging']['next']).json()
    for datum in my_likes['data']:
        me_object['likes']['data'].append(datum)

with open('my_likes.json', 'w', encoding='utf8') as makefile:
    json.dump(me_object, makefile, ensure_ascii=False, indent=4)

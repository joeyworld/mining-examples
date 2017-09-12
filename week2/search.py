import requests
import facebook
from prettytable import PrettyTable

ACCESS_TOKEN = 'EAACEdEose0cBALsX7DkHb5ZCmnVtHbtfyXuvCl2BpJwspHmHmEcce8mA5jJmqXWSMx9lawkLg2I4t3edurEPviOZAbpSsA7ZCLBQv6NkZCsQmpf33PXqpbmsK7ZBZC5KjJb3ZAvRx2bCn6EQfETy0FpDz5WZAWdXBiqRoObGLiVTbqUekJsMc6Q6hXA6O6QL97gZD'
api = facebook.GraphAPI(access_token=ACCESS_TOKEN)

args = {
    'type': 'page',
    'q': '건국대학교',
    'fields': 'name, likes'
}
search_result = api.request('search', args)
data = search_result['data']


def key(element):
    return element['likes']


while True:
    try:
        search_result = requests.get(search_result['paging']['next']).json()
        data += (search_result['data'])
    except KeyError:
        break

data = sorted(data, key=lambda datum: datum['likes'], reverse=True)
table = PrettyTable(field_names=['name', 'likes'])
for datum in data[:100]:
    table.add_row([datum['name'], datum['likes']])
print(table)

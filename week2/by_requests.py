import json
import requests

base_url = 'https://graph.facebook.com/me'
fields = 'id, name, friends'
access_token = 'EAACEdEose0cBALJsQsj6FnkDxcZCfmuG0EZCsIBZByawto' \
               'XGU0gwlGJc8pLoPZC0nrsqc5upMGQ5mre8opDsDVKMv0ZA1yBG' \
               'qxiSYU2mCDZClU1zHHZCMwmaG4fmOWZBQFZAo1jFVhQuPr1X4z' \
               '7z2vfeCgrqTaRgIJJHHUqarJGZAkzrgttBqm4AKjHYSWmPEdwGkZD'

response = requests.get('{}?fields={}&access_token={}'.format(base_url, fields, access_token))
print(response.status_code)
print(response.headers)
print(response.json())

response_json = {
    'Status': response.status_code,
    'Header': dict(response.headers),
    'Body': response.json()
}

with open('response.json', 'w', encoding='utf8') as file:
    json.dump(response_json, file, ensure_ascii=False, indent=2)

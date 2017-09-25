import json
import requests

response = requests.get('http://210.114.88.123?path=/dataset/Kdata/kdata_017/social.csv')
print(response.text)

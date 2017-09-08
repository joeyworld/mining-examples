import requests

# 뻐킹 소공
response = requests.get('http://dslab.konkuk.ac.kr/Class/2017/17SE/Team_Project_B.htm')
print(response.status_code)
print(response.headers)
print(response.text)

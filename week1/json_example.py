import json

data = {
    'name': '10cm',
    'members': [
        '권정열'
        # 윤철종 탈퇴함 ㅠㅠ
    ],
    'company': 'Magic Strawberry Sound',
    'genre': 'indie',
    'albums': {
        'regular': 4,
        'singles_ep': 6
    }
}

with open('10cm.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, indent=2, ensure_ascii=False)
    json_file.close()

with open('10cm.json', 'r', encoding='utf8') as json_file:
    loaded = json.load(json_file)
    for key, value in loaded.items():
        print('key: {}, value: {}'.format(key, value))
    json_file.close()

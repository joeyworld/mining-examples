from prettytable import PrettyTable

score = {
    "henry": [100, 90, 80],
    "james": [90, 90, 70],
    "todd": [50, 40, 100]
}

table = PrettyTable()

for key, value in score.items():
    row = [key]
    for item in value:
        row.append(item)
    table.add_row(row)

table.field_names = ['student', 'mathematics', 'english', 'science']
table.align = 'r'
table.align['student'] = 'c'
print(table)


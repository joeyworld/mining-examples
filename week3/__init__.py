a = [1, 2, 3, 4, 5]
length = len(a)
combinations = [(i, j) for i in range(length) for j in range(i, length)]
print(combinations)

# List comprehension examples

to_ten = [i for i in range(1, 11)]
evens = [i for i in range(1, 101) if i % 2 == 0]
print(to_ten)
print(evens)

words = ['pen', 'pineapple', 'apple', 'pie', 'banana']
e = [word for word in words if 'e' in word]
no_apple = [word for word in words if 'apple' not in word]
print(e)
print(no_apple)

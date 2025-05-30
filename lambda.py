#1
add = lambda x, y: x + y
print(add(3, 5))  # 8

#2
greet = lambda: "Hello, World!"
print(greet())  # Hello, World!

#3
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]

#4
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]

#5
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: x[1])
print(sorted_words)  # ['banana', 'date', 'apple', 'cherry']

#6
max_num = lambda a, b: a if a > b else b
print(max_num(10, 20))  # 20


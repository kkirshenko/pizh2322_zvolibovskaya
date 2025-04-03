number = [1, 2, 3, 4, 6, 9, 11, 15, 18]

result = sum(x**2 for x in number if x % 3 == 0)

print(result)

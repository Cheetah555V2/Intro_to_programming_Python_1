numbers = []
for num in range(1,101):
    numbers.append(num)

i = 2
while i < len(numbers):
    numbers.pop(i)
    i += 5

print(f"There are {len(numbers)} numbers left.")
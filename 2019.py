N = input("Enter1: ")
droid = input("Enter2: ")
numbers = list(map(int, (droid.split())))
print(numbers.pop(numbers.index(min(numbers))), min(numbers))

first = input()
numbers = first.split()
if int(numbers[0])<int(numbers[2]):
    x = int(numbers[0])
    x1 = int(numbers[2])
else:
    x = int(numbers[2])
    x1 = int(numbers[0])
if int(numbers[1])<int(numbers[3]):
    y = int(numbers[1])
    y1 = int(numbers[3])
else:
    y = int(numbers[3])
    y1 = int(numbers[1])

k = int(input())
n = 10**-9
if k>0:
    S = x1 - x
    m = S/(k+1)
    m = x1 - m
    S1 = y1 - y
    m1 = S1/(k+1)
    m1 = y1- m1
    print("{:.10f}".format(m), "{:.10f}".format(m1))
else:
    print()
from decimal import *
numbers = input().split()
if int(numbers[0])<=int(numbers[2]):
	x = int(numbers[0])
	x1 = int(numbers[2])
else:
	x = int(numbers[2])
	x1 = int(numbers[0])
if int(numbers[1])<=int(numbers[3]):
	y = int(numbers[1])
	y1 = int(numbers[3])
else:
	y = int(numbers[3])
	y1 = int(numbers[1])
	
k = int(input())
if k>0:
	getcontext().prec = 10
	S = x1 - x
	m = Decimal(S)/Decimal(k+1)
	m = Decimal(x1) - m
	S1 = y1 - y
	m1 = Decimal(S1)/Decimal(k+1)
	m1 = Decimal(y1)- m1
	print('{:.10f}'.format(m))
	print("{:.10f}".format(m1))

else:
	print('wrong input for k try again')
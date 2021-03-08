import random

print("Hello World")

# generate 10 random integers
def randomTenIntegers():
	for i in range(10):
		print(random.randint(0,10))

# generate a number of integers
def randomIntegers(numIntegers):
	for i in range(numIntegers):
		print(random.randint(0,numIntegers))



randomIntegers(15)


import random

# random.randint(min, max)
print("hello world")

#function for generating 10 random numbers
def randomTenNumbers():
	for i in range(10):
		print(random.randint(0,10))
	print("end of function")

#function for generating a given number random numbers
def randomNumbers(numGens, nMax):
	for i in range(numGens):
		print(random.randint(0,nMax))
	print("end of function")



randomNumbers(100,1000)

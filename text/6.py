def squareForSqrt(number1, number2 = 2):
	return number1 ** number2

def squareRoot(number1):
	sqrt = squareForSqrt(number1, 1/2.0)
	if sqrt % 1 == 0:
		return int(sqrt)
	else:
		return int(sqrt) + 1

def isDivisible(number1, number2):
	if(number1 % number2 == 0):
		return True
	else:
		return False

def isPrime(number):
	case = True
	if(number == 2):
		return True
	for i in range(2,(squareRoot(number)+1)):
		if number % i == 0:
			return False
		else:
			case = True
	return case

def firstMPrimes(number):
	a = []
	runner = 2 
	counter = 0
	while(counter <  number):
		if(isPrime(runner)):
			a.append(runner)
			runner += 1
			counter += 1
		else:
			runner +=1
	return a

print(isPrime(16))
print(firstMPrimes(8))



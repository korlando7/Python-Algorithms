#finds nth fibonacci number in the sequence using python3

n = int(input("Enter number: "))

def fibonacci(n):

	#first two numbers in the sequence
	a, b = 0, 1

	if n<=1:
		return n

	for i in range(0, n-1):
		a, b = b, a+b

	if n % 10 == 1:
		return ("The " + str(n) + "st number in the Fibonacci sequence is " + str(a))
	elif n % 10 == 2:
		return ("The " + str(n) + "nd number in the Fibonacci sequence is " + str(a))
	elif n % 10 == 3:
		return ("The " + str(n) + "rd number in the Fibonacci sequence is " + str(a))
	else:
		return ("The " + str(n) + "th number in the Fibonacci sequence is " + str(a))

print (fibonacci(n))

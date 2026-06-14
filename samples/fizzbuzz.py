def fizz(number):
	return number % 3 == 0

def buzz(number):
	return number % 5 == 0

def fizzbuzz(number):
	return number % 15 == 0

start = 1
end = 50
for number in list(range(start, end + 1)):
	if fizzbuzz(number):
		print("FizzBuzz")
	elif fizz(number):
		print("Fizz")
	elif buzz(number):
		print("Buzz")
	else:
		print(number)

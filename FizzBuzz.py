def funcFizzBuzz(n):
	# for-in loop for range 
	for i in range(1, n + 1):
		# divisble by 3 and 5
		if i % 3 == 0 and i % 5 == 0:
			print("FizzBuzz")
		# divisble by 3
		elif i % 3 == 0:
			print("Fizz")
		# divisble by 5
		elif i % 5 == 0:
			print("Buzz")
		# not divisble by 3 or 5
		elif i % 3 != 0 or i % 5 != 0:
			print(str(i))

# call the funcFizzBuzz function
funcFizzBuzz(5)

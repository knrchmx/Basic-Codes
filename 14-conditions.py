#==================={Conditions/ControlFlow}=====================#

#Control flow - gives us this ability to choose among outcomes.
#def - a function defined in Python.

#ExampleCodeWithoutContext
def yourself():
	print("You're now trapped inside a box.")
	print("Will you stay inside or go outside?")
	
	answer = input("Type inside or outside and hit 'Enter'.").lower()

	if answer == "inside" or answer == "i":
		print("---------------------")
		print("You suffocated yourself and die.")
		print("---------------------")
		input("Press ENTER to exit.")
	elif answer == "outside" or answer == "o":
		print("---------------------")
		print("It's very dark and cold outside, you can't see anything")
		print("until a blunt object hit your head and you died instantly.")
		print("---------------------")
		input("Press ENTER to exit.")
	else:
		print("---------------------")
		print("Please make your choice correctly.")
		yourself()

yourself()

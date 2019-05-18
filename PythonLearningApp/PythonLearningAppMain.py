def helloWelcome():
	welcomeMessage = "Welcome to the world of Python Learning !!! What is your name ?"
	print(welcomeMessage)
	name = input()
	firstQ = "how can I help you ?"
	secondQ = "Do you want me to help with \" "
	
	if(name == "Suresh"): 
		print("Hello Suresh you are great,",firstQ)
	elif(name == "Ramesh"):
		print("Hello Ramesh you are a great learner,",firstQ)
	elif(name == "Bhala"):
		print("Hello Bhala good to see you, appreciate your interest to learn Python,",firstQ)
	else:
		print("Hello",name,firstQ)
		
	firstAnswer = input()
	print(secondQ,firstAnswer,"\"?")
	
	if(firstAnswer == "operations"):
		print("What operation do you want to do, enter one of the symbols (+,-,*,/):")
		operation = input()
		if (operation == "+"):
			print("Please enter the first number to add ")
			inputNumber1 = int(input())
			inputNumber2 = int(input("Enter the second number please"))
			print("The result of",inputNumber1,"+",inputNumber2,"=",add(inputNumber1,inputNumber2))
		elif(operation == "-"):
			print("Please enter the first number to subtract")
			inputNumber3 = int(input())
			inputNumber4 = int(input("Enter the second number please"))
			print("The result of",inputNumber3,"-",inputNumber4,"=",subtract(inputNumber3,inputNumber4))
		# elif(operation == "*"):
		    # print("Please enter the first number to multiply")
			# inputNumber1 = int(input())
			# inputNumber2 = int(input("Enter the second number please"))
			# print("The result of",inputNumber1,"+",inputNumber2,"=",multiply(inputNumber1,inputNumber2))
		 # elif(operation == "/"):
		    # print("Please enter the first number to divide")
			# inputNumber1 = int(input())
			# inputNumber2 = int(input("Enter the second number please"))
			# print("The result of",inputNumber1,"+",inputNumber2,"=",divide(inputNumber1,inputNumber2))
		else :
			print("This operation is still not supported, Thank you please come back later")	
	else :
		print("This feature is still not supported, Thank you please come back later")
			

def add(n1,n2):
	print(n1,"+",n2)	
	return n1+n2
	
def subtract(n1,n2):
	print(n1,"-",n2)	
	return n1-n2
	
def main():	
	helloWelcome()
	print("*****************************************")
	
main()
number1 = int(input("Enter a number: "))

number2 = int(input("Enter a number again: "))

operation =int(input("Enter an operation number:\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division"))


if operation == 1:
    result=number1 + number2
elif operation == 2:
    result = number1 - number2
elif operation == 3:
    result = number1*number2
elif operation == 4:
    result = number1/number2
else:
    result = "Invalid operation"

print("The resul is: ", result)


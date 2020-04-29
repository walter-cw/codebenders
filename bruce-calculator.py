option = """
(1) addition
(2) subtraction
(3) multiplication
(4) division
(5) finding fibonacci numbers
(6) summation of numbers those are less or equal than given number
"""


while True:
  question = input("Enter the number of option you want to do (enter q to quit): ") 
  if question == "q":
    break
  elif question == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "+", num2, "=", num1 + num2)
  elif question == "2":
    num3 = int(input("Enter first number: "))
    num4 = int(input("Enter second number: "))
    print(num3, "-", num4, "=", num3 - num4)
  elif question == "3":
    num5 = int(input("Enter first number: "))
    num6 = int(input("Enter second number: "))
    print(num5, "*", num6, "=", num5 * num6)
  elif question == "4":
    num7 = int(input("Enter first number: "))
    num8 = int(input("Enter second number: "))
    print(num7, "/", num8, "=", num7 / num8)
  elif question == "5":
    num9 = int(input("Enter the upper limit of fibonacci number: "))
    ls = [1]
    a = 0
    b = 1
    c = 1
    while c < num9:
      c = a+b
      a = b
      b = c
      ls.append(b)
    print(ls)
  elif question == "6":
    num10 = int(input("Enter a number: "))
    summ = 0
    for i in range(num10+1):
      if i%3 == 0 and i%5 ==0:
        summ += i
    print(summ)
  else:
    print("Wrong option!")
    print("Enter one of these options:", option)

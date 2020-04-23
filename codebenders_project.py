while True:

    print("""
    Welcome to calculater.
    Please select your operation;
    
    1. Calculater
    2. Fibonacci
    3. Find sum of numbers that can divided by 5 or 3
    Q . Press q for quit.
    
    """)

    op = input("Please select your operation 1, 2, 3, q: ").strip().lower()

    if op == "q":
        print("See you later. Program is closing.")
        break
    elif op == "1":
        while True:

            print("""
            CALCULATER
    Please select your operation:
        1. Addition
        2. Substraction
        3. Multiplication
        4. Division
        Q. Pres q for quit
            """)

            select = input("Please enter your operation 1, 2, 3, 4, q: ").lower().strip()
            if select == "q":
                print("This calculation ended")
                break

            elif select not in ("1", "2", "3", "4"):
                print("Invalid choise!")

            else:
                num1 = int(input("Enter a first number: "))
                num2 = int(input("Enter a second number: "))

                if select == "1":
                    print("{} + {} = {}".format(num1, num2, num1 + num2))

                elif select == "2":
                    print("{} - {} = {}".format(num1, num2, num1 - num2))

                elif select == "3":
                    print("{} * {} = {}".format(num1, num2, num1 * num2))

                else:
                    try:
                        if num1 % num2 == 0:
                            print("{} / {} = {}".format(num1, num2, num1 // num2))
                        else:
                            print("{} / {} = {:.2f}".format(num1, num2, num1 / num2))
                    except ZeroDivisionError:
                        print("Numbers can't diveded by zero")

    elif op == "2":

        while True:

            print("""
               FIBONACCI
    Press q for guit this operation\n
            """)
            num = input("Enter a number: ").lower().strip()

            if num == "q":
                print("This calculation ended")
                break

            else:
                num = int(num)
                a = 1
                b = 1
                fibonacci = [a, b]

                while len(fibonacci) < num:
                    a, b = b, a + b
                    fibonacci.append(b)
                print(*fibonacci)

    elif op == "3":

        while True:
            print("""
              SUM OF NUMS
    Press q for quit this operation\n
            """)
            num = input("Please enter a number: ").lower().strip()
            summ = 0

            if str(num) == "q":
                print("This calculation ended")
                break

            else:
                num = int(num)
                for i in range(num + 1):
                    if i % 3 == 0 or i % 5 == 0:
                        summ += i
            print("Sum of numbers = {}".format(summ))

    else:
        print("Invalid operation!!")

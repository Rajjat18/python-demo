num1 = int (input("Enter First Number: "))
num2 = int (input("Enter Second Number: "))

choice = input("Enter the operatin option (+, -, *, /): ")
if choice == "+":
    sum_of_num = num1 + num2

    print("Addition : ",sum_of_num)

elif choice == "-":
    sub_of_number = num1 - num2
    print("subtraction :" ,sub_of_number)

elif choice == "*":
    multiply_of_num = num1 * num2
    print("multiplication : ",multiply_of_num)

elif choice == "/":
     print("divide :" ,divide_of_number)
     divide_of_number = num1 / num2

else:
    print("inalid Choice")
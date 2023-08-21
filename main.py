num1 = int(input("enter the first number:   "))
num2 = int(input("enter your second number:   "))
op = int(input("please enter a number endicating an  operation \n 1)addition \n 2)subtraction \n 3)multiplication \n 4)division \n "))


def calculate(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 4:
        return num1 / num2
    

      





print(calculate(num1, num2, op))

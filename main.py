num1 = int (input ("Enter the number:"))
num2 = int(input("Enter the number:"))
op = int(input("please enter a number endicating an  operation \n 1)addition \n 2)subtraction \n 3)multiplication \n 4) division"))
def calculate(num1, num2, op):   
        if op==2:
          return num1-num2  
        elif op==1:
          return num1+num2
        elif op==3:
          return num1*num2
        elif op==4:
          return num1/num2
        print(calculate(num1, num2, op))
        

import os
def sum(number1,number2):
    return number1+number2
def sub(number1,number2):
    return number1-number2
def mult(number1,number2):
    return number1*number2
def div(number1,number2):
    return number1/number2            


def calculator():
    num1 =int(input("Enter the first number: "))
    should_continue=True
    while should_continue:
        op =input("Pick an operation!\n+\n-\n*\n/\n")
        num2 =int(input("Please enter the second number: "))
        if op=="+":
            ans =sum(num1,num2)
        elif op=="-":
            ans =sub(num1,num2)
        elif op=="*":
            ans =mult(num1,num2)
        elif op=="/":
            ans =div(num1,num2)
        else:
            print("Invalid Input")
        print(ans)
        out =input(f"Type y to continue with {ans} or type n to start a new calculator")
        if out =="y":
            num1 =ans
        else:
            should_continue=False
            os.system('cls')
            calculator() 
calculator()        

        



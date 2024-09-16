import cmath

def get_opperator(v1, v2):
    for i in range(len(v2)):
        if v1.lower() == v2[i]:
            return True
    else:
        return False
        
def damath(num1, opperator, num2=0):
    if opperator == "add":
        return num1,"+",num2,"=",num1+num2
    elif opperator == "subtract":
        return num1,"-",num2,"=",num1-num2
    elif opperator == "multiply":
        return num1,"*",num2,"=",num1*num2
    elif opperator == "divide":
        return num1,"/",num2,"=",num1/num2
    elif opperator == "exponent":
        return num1,"to the power of",num2,"=",num1**num2
    elif opperator == "square root":
        answer = cmath.sqrt(num1)
        return "The square root of",num1,"is",answer
    else:
        return "ERROR"

        

print("Welcome to my Calculator!")
while True:
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            break
        except:
            print("That is not a number!")


    acceptable_opperators = ["add", "subtract", "multiply", "divide", "exponent", "square root"]
    while True:
        opperator = input("Enter an opperator (add, subtract, multiply, divide, exponent, square root): ")
        if get_opperator(opperator, acceptable_opperators) == True:
            break
        else:
            print("That is not an opperator!")

    num2 = 0
    if opperator != "square root":
        while True:
            try:
                num2 = int(input("Enter the second number: "))
                if num2 == 0 and opperator == "divide":
                    print("You cannot use zero as a denominator!")
                else:
                    break
            except:
                print("That is not a number!")

    print(damath(num1, opperator, num2))



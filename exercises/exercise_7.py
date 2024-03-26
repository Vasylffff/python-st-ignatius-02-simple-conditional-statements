# Your solution to Exercise 7
a = float(input())
b = float(input())
calculation= (input())
if calculation == "+":
    print (a+b)
elif(calculation == "-"):
    print(a-b)
elif(calculation == "*"):
    print(a*b)
elif(calculation == "/"):
    if(b==0):
        print("Division by 0!")
    else:
        print(a/b)
elif  calculation == "pow":
    print(a**b)
elif calculation == "mod":
    print(a%b)
     

     

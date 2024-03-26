# Your solution to Exercise 5

a = float(input())
b = float(input())
c = float(input())
if(a!= 0 and b !=0 and c !=0):
        if b*b-4*a*c > 0:
            x1 = int(((-b + (b*b-4*a*c) ** 0.5) / (2 * a))*100)/100
            x2 = int(((-b - (b*b-4*a*c) ** 0.5) / (2 * a))*100)/100
            print(f"{x1} and {x2}")
        elif b*b-4*a*c == 0:
            x = -b / (2 * a)
            print(f"{x}h")
        else:
            print("No roots")
else:
    print("Infinite roots")
    

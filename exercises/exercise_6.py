# Prompt user to enter coordinates of A and B
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

# Calculate the distance between A and B
d1 = (x1**2+y1**2) 
d2 = (x2**2+y2**2)

# Print the distance between A and B
if d1 > d2:
    print("A is further from the origin.")
elif d1 < d2:
    print("B is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")


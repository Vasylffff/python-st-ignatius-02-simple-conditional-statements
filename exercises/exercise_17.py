# Your solution to Exercise 17
"""
a = 10

if a % 2 == 0:
   if  a < 5:
       print("2")
elif a%3 == 0:
   print("3")
   """

salah_is_open = True
mane_is_open = False
message = "Pass to Salah" if salah_is_open else "Pass to Mané" if mane_is_open else "Neither Salah nor Mané is open"

if salah_is_open:
    message = "Pass to Salah" 
elif mane_is_open:
    message = "Pass to Mané" 
else:
    message = "Neither Salah nor Mané is open"


print(message)
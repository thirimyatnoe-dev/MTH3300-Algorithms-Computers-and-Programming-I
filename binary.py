import random

#user input for the base 2 numbers
d1 = int(input("Enter 8's digit: "))
d2 = int(input("Enter 4's digit: "))
d3 = int(input("Enter 2's digit: "))
d4 = int(input("Enter 1's digit: "))

#calculation for Base 10 number
base10num = (d1* (2**3)) + (d2* (2**2)) + (d3* (2**1)) + (d4* (2**0))

print(f"The binary number {str(d1)+str(d2)+str(d3)+str(d4)} is {base10num} in base ten")

#generating random numbers between 0 and 15 inclusive
x = random.randrange(0,15)

#comparing the base 10 number with the randomly generated number
print(f"Less than the randomly generated number {x}?", end=" ")
if base10num < x:
    print(True)
else:
    print(False)

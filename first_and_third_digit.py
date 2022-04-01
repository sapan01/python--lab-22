# Print the sum of first and third digits of a number

a = input("Enter a no.: ")
try:
    first = int(a[0])
    third = int(a[2])
    print("Sum of first and third digits =", first+third)
except:
    print("Invalid no.!")

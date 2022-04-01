# Print multiples of a number within a range and whether they are even or odd

n = int(input("Enter a no. n: "))
m = int(input("Enter the value of m: "))

for i in range(1, n+1):
    if i % m == 0:
        print(i, end=" ")
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")

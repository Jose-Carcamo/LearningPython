number = 0
total = 0
numbers = ""
while number <=0:
    number = int(input("Enter a positive number: "))
    if number <= 0:
        print("Invalid number. Try again.")
    else:
        for x in range(1,number+1):
            numbers += str(x) + " "
            total = total + x
print("Numbers:",numbers)
print(f"Sum: {total}")
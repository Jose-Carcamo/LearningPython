Enter = int(input("How many numbers will you enter? "))
Sum = 0
Digits = []
for x in range(1, Enter + 1):
    Number = int(input(f"Enter number {x}: "))
    while Number <=0:
        Number = int(input("Invalid number. Try again. "))
    Sum += Number
    Digits.append(Number)
Average = Sum/Enter
formatted_numbers = " ".join(str(n) for n in Digits)
print(f"Numbers: {formatted_numbers}")
print(f"Sum: {Sum}")
print(f"Average: {Average:.2f}")
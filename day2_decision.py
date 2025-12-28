age = int(input("What is your age? "))
student = input("Are you a student? (yes/no) ").lower()
if student == "yes":
    student = 1
else:
    student = 0
if age < 12:
    price = 5
elif age >= 12 and student:
    price = 8
else:
    price = 12
print(f"Your ticket price is ${price}.")
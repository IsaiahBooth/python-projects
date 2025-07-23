password = ""

while password != "python":
    password = input("Enter the secret password")

    if password != "python":
        print("Wrong password try agin!")

print("Correct password! Welcome")

print("Next") 

total = 0
number = 1

print("enter numbers to add up. Enter 0 to stop")

while number != 0:
    number = int(input("Enter a number: "))

    if number != 0:
        total = total + number
        print(f"Running total: {total}")

print(f"Final total: {total}")
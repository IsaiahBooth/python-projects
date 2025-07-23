for i in range(5):
    print(f"this is loop number {i}")

print("NEXT")

for i in range(1, 11):
    print(f"{i}")


print ("NEXT")

favfood = ["burger", "chips", "pizza"]
for food in favfood:
    print (f"{food}")

print("NEXT")

for num in range(0, 21, 2):
    print(f"Enen Number {num}")


print ("NEXT")

for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")

print("NEXT")

word = "PYTHON"

for letter in word:
    print (f"Letter: {letter}")

print(f"the word '{word}' has {len(word)} letters!")

print("NEXT")

for row in range(3):
    print(f"Row {row + 1}: ", end="")

    for star in range(5):
        print("* ", end="")

    print()

print("NEXT")

times = int(input("How many times should I say hello"))

for i in range(times):
    print(f"hello #{i + 1}!")

print("all done saying hello!")
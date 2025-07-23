row = int(input("rows"))
column = int(input("columns"))

for rows in range(row):
    print(f"* ", end="")

    for columns in range(column - 1):
        print("* ", end="")

    print()
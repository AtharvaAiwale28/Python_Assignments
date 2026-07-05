
x = int(input("Enter a number: "))
match x:
    case 0:
        print("You entered zero.")
    case 1:
        print("You entered one.")
    case _:
        print(f"You entered something else: {x}")
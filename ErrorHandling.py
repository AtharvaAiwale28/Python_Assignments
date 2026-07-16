a = input("Enter a number: ")
try:
    print(f"Multiplication table of {a} is:")
    a = int(a)
    for i in range(1, 11):
        print(f"{a} X {i} = {a * i}")
except:
    print("Please enter a valid number.")

print("some important lines of code")
print("end of the program")

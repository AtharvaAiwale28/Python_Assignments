# a = input("Enter a number: ")
# try:
#     print(f"Multiplication table of {a} is:")
#     a = int(a)
#     for i in range(1, 11):
#         print(f"{a} X {i} = {a * i}")
# except:
#     print("Please enter a valid number.")

# print("some important lines of code")
# print("end of the program")

try:
    num = int(input("Enter a Number:"))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Please enter a valid Number.")
except IndexError:
    print("Index out of range.")
except Exception as e:
    print(f"An error occurred: {e}")


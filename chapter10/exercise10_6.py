first_number_str = input("Please input first number:")
try:
    first_number = int(first_number_str)
except ValueError as e:
    print("You input wrong number!")
    first_number = 0

second_number_str = input("Please input second number:")
try:
    second_number = int(second_number_str)
except ValueError as e:
    second_number = 0
    print("You input wrong number!")
print(first_number + second_number)


from modul import get_median
# Exapmle input: 1,2,3,4,5
user_input = input("Please enter numbers separated by ,\nhere:")

try:
    print(f"Median is {get_median(user_input.split(','))}")
except Exception as e:
    print(f"An error occured \n{e}")

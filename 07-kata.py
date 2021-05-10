def show_negative_numbers(numbers):
    for num in numbers:
        if num < 0:
            print(num, end=" ")

numbers = [11, -21, 0, 45, 66, -93]
show_negative_numbers(numbers)
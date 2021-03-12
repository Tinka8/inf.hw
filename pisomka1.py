def every_odd_number(num_list):
    output = []

    for number in num_list:

        if number % 2:
            output.append(number)

    return output

print(every_odd_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(every_odd_number([1, 4, 7, 5, 9, 11, 2]))

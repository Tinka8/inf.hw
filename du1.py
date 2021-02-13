# variables and arrays 
value = 0
numbers = []


# append number to numbers array
while value < 10:
    number = int(input("zadaj číslo: "))
    numbers.append(number)

# if number is divisible by 3 with 0 rest then enlarge value by 1 
    if number % 3 == 0:
        value += 1
       

print(sum(numbers))
print(*numbers)

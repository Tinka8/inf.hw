number_from = int(input("od: ")) # interval "od"
number_to = int(input("do: ")) # interval "do"
exponentials = [1, 3, 5, 7]

# for each number
for number in range(number_from, number_to + 1):
    line = " "

    # for each exponent
    for exponential in exponentials:
        line = line + str(pow(number, exponential)) + " "

    print(line)

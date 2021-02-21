n = int(input("write a number: "))

for row in range(1,n + 1):
    line = " "

    for col in range(0,n):
        line = line + str(row + (col * n)) + " "


    print(line)
    

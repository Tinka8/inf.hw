# variables
total = 0

# define num 
while True:
    operation = input("zadaj operáciu(+-/*): ")

# write koniec ends program
    if operation == "koniec":
        break

# otherwise we use + and retype variable total
    elif operation == "+":
        num = float(input("zadaj číslo: "))   
        subtotal = total + num
        print(total, "+", num, "=", subtotal)
        total = subtotal

# otherwise we use - and retype variable total
    elif operation == "-":
        num = float(input("zadaj číslo: "))
        subtotal = total - num
        print(total, "-", num, "=", subtotal)
        total = subtotal

# otherwise we use / and retype variable total 
    elif operation == "/":
        num = float(input("zadaj číslo: "))
        subtotal = total / num
        subtotal= round(subtotal, 2)
        print(total, "/", num, "=", subtotal)
        total = subtotal

# otherwise we use * and retype variable total
    elif operation == "*":
        num = float(input("zadaj číslo: "))
        subtotal = total * num
        print(total, "*", num, "=", subtotal)
        total = subtotal
        
        


# premenná
celkom = 0

# definujeme operaciu a určíme podmienku
while True:
    operacia = input("zadaj operáciu(+-/*): ")

# koniec skončí program
    if operacia == "koniec":
        break

# + sčíta čísla a prepíše celkom
    elif operacia == "+":
        cislo = float(input("zadaj číslo: "))   
        subtotal = celkom + cislo
        print(celkom, "+", cislo, "=", subtotal)
        celkom = subtotal

# - odčíta čísla a prepíše celkom
    elif operacia == "-":
        cislo = float(input("zadaj číslo: "))
        subtotal = celkom - cislo
        print(celkom, "-", cislo, "=", subtotal)
        celkom = subtotal

# / vydelí čísla a prepíše celkom 
    elif operacia == "/":
        cislo = float(input("zadaj číslo: "))
        subtotal = celkom / cislo
        subtotal= round(subtotal, 2)
        print(celkom, "/", cislo, "=", subtotal)
        celkom = subtotal

# * vynásobí čísla a prepíše celkom
    elif operacia == "*":
        cislo = float(input("zadaj číslo: "))
        subtotal = celkom * cislo
        print(celkom, "*", cislo, "=", subtotal)
        celkom = subtotal
        

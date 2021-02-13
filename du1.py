# premenné a polia 
hodnota = 0
cisla = []


# pridava cislo do pola cisla
while hodnota < 10:
    cislo = int(input("zadaj číslo: "))
    cisla.append(cislo)

# ked je cislo delitelne 3 s 0 zvyskom zvysi sa hodnota o 1 
    if cislo % 3 == 0:
        hodnota += 1
       

print(sum(cisla))
print(*cisla)

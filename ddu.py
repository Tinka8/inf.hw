n = int(input('zadaj cele nezaporne cislo: '))
znak1 = str(input('zadaj jednoznakovy retazec: '))
znak2 = str(input('zadaj druhy jednoznakovy retazec: '))

for line in range(1, n+1):

    for col in range(1, n+1):

        if line == 1:                   # horna strana
            print(znak1, end = '')
        elif col == 1:                  # lava strana
            print(znak1, end = '')
        elif line == n:                 # dolna strana
            print(znak1, end = '')
        elif col == n:                  # prava strana
            print(znak1, end = '')
        elif col == line:               # uhlopriecka zlava hore dolu doprava
            print(znak1, end = '')
        elif col == ((n + 1) - line):   # uhlopriecka sprava hore dolu dolava
            print(znak1, end = '')
        else:                           # ostatne
            print(znak2, end = '')
    
    print('')

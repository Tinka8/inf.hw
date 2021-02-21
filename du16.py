n = int(input("write a number: "))

for i in reversed(range(0,n+1)):

    line = ""
    for c in range(1,i+1):
        line = line + str(c) + " " 
        

    print(line)
    




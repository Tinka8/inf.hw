def every_second_number(num_list):
    last_printed = False
    
    for number in num_list:
        
        if last_printed == False:
            print(number)
            last_printed = True
        else:
            last_printed = False
def max_pair_sum(num_list):

    if len(num_list) < 2:
        return 'Nedava smysl'

    previous = 0
    maximum = 0

    for number in num_list:
        current_sum = number + previous
        previous = number
        
        if current_sum > maximum:
            maximum = current_sum
    
    return maximum
def get_maximum_tenants(houses):

    # maximum tenants
    maximum = 0 # stores maximum tenants in one house
    for house in houses:
        if house > maximum:
            maximum = house

    # maximum tenants count
    maximum_count = 0 # store number of houses with maximum tenants
    for house in houses:
        if house == maximum:
            maximum_count += 1

    print('maximalny pocet obyvatelov v dome je ' + str(maximum))
    print('pocet maximalnych domov je ' + str(maximum_count))

get_maximum_tenants([4, 2, 0, 5, 0, 1, 5, 4])

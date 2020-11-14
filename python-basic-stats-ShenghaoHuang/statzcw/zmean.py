def mean(list_in):
    counter = 0
    total = 0
    for i in list_in:
        total += i
        counter += 1
    return round(float(total / counter), 2)


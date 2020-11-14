def median(list_in):
    list_in = sorted(list_in)
    if len(list_in) % 2 == 0:
        middle = len(list_in) / 2
        mid1 = list_in[int(middle)]
        mid2 = list_in[int(middle-1)]
        mid = (mid1 + mid2) / 2
        return mid
    elif len(list_in) % 2 != 0:
        mid = int(len(list_in) / 2)
        return list_in[mid]





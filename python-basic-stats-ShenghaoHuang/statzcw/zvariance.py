def variance(list_in):
    mean = (sum(list_in) / len(list_in))
    mean_2 = [i-mean for i in list_in]
    square = [i**2 for i in mean_2]
    vari = sum(square) / (len(list_in)-1)
    return round(vari,2)


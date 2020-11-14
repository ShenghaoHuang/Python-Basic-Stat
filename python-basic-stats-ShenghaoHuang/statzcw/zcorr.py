import statzcw.zmean as zmean, statzcw.zstddev as zdev

def covariance(list_x, list_y):
    sum = 0
    N = len(list_x)
    x_mean = zmean.mean(list_x)
    y_mean = zmean.mean(list_y)
    x_dev = zdev.stddev(list_x)
    y_dev = zdev.stddev(list_y)
    for i in range(0, len(list_y)):
        sum += (list_x[i] - x_mean) * (list_y[i] - y_mean)
    covar = sum/(N-1)
    cor = round(covar / (x_dev * y_dev), 3)
    return cor
    #print(f'Covariance is {covar} and Correlation is {cor}')

# x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
# y = [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]
#
# covariance(x,y)
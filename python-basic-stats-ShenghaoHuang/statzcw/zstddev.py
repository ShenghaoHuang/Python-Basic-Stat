import statzcw.zvariance as zv
import math

def stddev(list_in):
    vari = zv.variance(list_in)
    dev = math.sqrt(vari)
    return round(dev, 2)



import statzcw.zstddev as zs
import statzcw.zvariance as zv
import math


def stdderr(list_in):
    dev = zs.stddev(list_in)
    err = dev / math.sqrt(len(list_in))
    return round(err, 2)

# print(zv.variance([600, 470, 170, 430, 300]))
# print(zs.stddev([600, 470, 170, 430, 300]))
# print(stdderr([600, 470, 170, 430, 300]))



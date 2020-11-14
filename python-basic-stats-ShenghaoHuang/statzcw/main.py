import csv
from statzcw import zcount
from statzcw import zmean
from statzcw import zmode
from statzcw import zmedian
from statzcw import zvariance
from statzcw import zstderr
from statzcw import zstddev
from statzcw import zcorr

dataOne = '/Users/sheng/Projects/python-basic-stats-ShenghaoHuang/dataOne.csv'
dataTwo = '/Users/sheng/Projects/python-basic-stats-ShenghaoHuang/dataTwo.csv'
dataThree = '/Users/sheng/Projects/python-basic-stats-ShenghaoHuang/dataThree.csv'
dataZero = '/Users/sheng/Projects/python-basic-stats-ShenghaoHuang/dataZero.csv'

def csv_reader(file):
    reader = csv.DictReader(open(file))
    result = {}
    for row in reader:
        for column, value in row.items():
            result.setdefault(column, []).append(float(value))
    return result

test = csv_reader(dataOne)

x = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y = [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]

print("Count")
print(zcount.count(x))
print("Mean")
print(zmean.mean(x))
print("Mode")
print(zmode.mode(x))
print("Median")
print(zmedian.median(x))
print("Variance")
print(zvariance.variance(x))
print("Standard Deviation")
print(zstderr.stdderr(x))
print("Standard Error")
print(zstddev.stddev(x))
print("Correlation")
print(zcorr.covariance(x, y))

import sys

date = [31,28,31,30,31,30,31,31,30,31,30,31]

m = 500
k = 0
i = 0
apple = 3
pear = 5
month = 0

while i<m:
    if k%2==0: i+=apple
    if k%3==0: i+=pear
    k += 1

while True:
    if month>12: month = 0
from datetime import date, timedelta
d = date(1901, 1, 6)

sum = 0
while d < date(2001, 1, 1):
    d += timedelta(7)
    if d.day == 1:
        sum += 1
print(sum)
import csv

with open('nurse_attrition.csv') as data:
    reder = csv.DictReader(data)
    rec = list(reder)

    dist = [int(record['DistanceFromHome']) for record in rec]
    maz = max(dist)
    print(maz)

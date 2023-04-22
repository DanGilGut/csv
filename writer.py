import csv

QuotaAmount = "160000"
StartDate = "2023-01-01"
OwnerName = "Chris Riley"
Username = "trailhead9.ub20k5i9t8ou@example.com"
# myData = ["160000" + "2023-01-01" + "Chris Riley" + "trailhead9.ub20k5i9t8ou@example.com"]
myData = ["\n{},{},{},{}".format(QuotaAmount, StartDate, OwnerName, Username)]
myFile = open('archivo_ejemplo.csv', 'a')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows([myData])

print("Writing complete")

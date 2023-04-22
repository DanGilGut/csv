import csv
with open('archivo_ejemplo.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
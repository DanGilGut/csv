# Maper como un diccionario

import csv

results = []
with open('archivo_ejemplo.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print(results)

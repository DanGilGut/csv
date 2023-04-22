data = [{'QuotaAmount': '150000', 'StartDate': '2016-01-01', 'OwnerName': 'Chris Riley',
         'Username': 'trailhead9.ub20k5i9t8ou@example.com'},
        {'QuotaAmount': '150000', 'StartDate': '2016-01-01', 'OwnerName': 'Chris Riley',
         'Username': 'trailhead9.ub20k5i9t8ou@example.com'}]

import csv

with open('archivo_ejemplo.csv', 'w') as csvfile:
    fieldnames = ['QuotaAmount', 'StartDate', 'OwnerName', 'Username']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'QuotaAmount': '160000', 'StartDate': '2016-01-01', 'OwnerName': 'Chris Riley',
                     'Username': 'trailhead9.ub20k5i9t8ou@example.com'})
    writer.writerow({'QuotaAmount': '160000', 'StartDate': '2016-01-01', 'OwnerName': 'Chris Riley',
                     'Username': 'trailhead9.ub20k5i9t8ou@example.com'})
print("Writing complete")

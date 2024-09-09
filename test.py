import csv

sk = "tehran"

with open('./Assets/worldcities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[0].lower() == sk.lower():
            lat=row[1]
            lng=row[2]
            break
        
print(lat, lng)
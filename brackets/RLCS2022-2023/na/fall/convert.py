import csv

with open('regional2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[1][1:].replace(' ', '-')
        f = open(name+'.json', "w")
        f.write("{\"team\": \"" + row[1][1:] +"\", \"url\": \""+ row[0]+ "\"}")
        f.close()
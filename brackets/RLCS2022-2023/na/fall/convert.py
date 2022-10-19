import csv

with open('regional1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        name = row[1][1:].replace(' ', '-')
        f = open(name+'.json', "w")
        f.write("{\"team\": \"" + row[0] +"\", \"url\": \""+ row[1][1:]+ "\"}")
        f.close()
import json
import csv

parlamentarios = dict()

with open('congreso_refined.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        print row[0]        
        id = row[5]
        nombre = row[2]
        parlamentarios[id] = dict()
        parlamentarios[id]['name'] = nombre
        parlamentarios[id]['page'] = row[1] 
        parlamentarios[id]['foto_src'] = row[27]
        parlamentarios[id]['group'] = row[11]
        parlamentarios[id]['province'] = row[8]
        parlamentarios[id]['role_or_group'] = row[11]
      
        parlamentarios[id]['seat_code'] = row[0]
        parlamentarios[id]['seat_coords'] = (row[3], row[4])        

with open('parlamento_de_navarra.json', 'w') as outfile:
    json.dump(parlamentarios, outfile)

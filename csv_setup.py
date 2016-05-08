import csv

prop_headers = ['identifier', 'sex', 'age', 'weight(kg)', 'height(cm)',
 'alcohol', 'ihd', 'hypertension', 'sleep apnoea', 'diabetes',
  'cvd', 'dementia','asa', 'procedure(p,c,d)', 'start', 'finish',
   'last dose time', 'total dose(mg)', 'n/v', 'pain', 'tolerating',
     'ready for discharge', 'aldrete', 'time discharge assessment']

def go():
    with open('propofol_data.csv', 'ab') as csvfile:
        datawriter = csv.writer(csvfile, dialect='excel')
        datawriter.writerow(prop_headers)
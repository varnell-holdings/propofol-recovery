import csv

prop_headers = ['patient/control', 'identifier', 'sex', 'age', 'weight', 'height',
 'alcohol', 'ihd', 'hypertension', 'sleep apnoea', 'diabetes',
  'cvd', 'dementia','asa', 'procedure', 'start', 'finish',
   'last dose time', 'total dose', 'n/v', 'pain', 'tolerating',
     'ready for discharge', 'aldrete', 'time discharge assessment']

def go():
    with open('data.csv', 'ab') as csvfile:
        datawriter = csv.writer(csvfile, dialect='excel')
        datawriter.writerow(prop_headers)
if __name__ == '__main__':
    go()
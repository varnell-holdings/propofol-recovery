import csv, re, click

# using 2.7 in conda env 'propofol'

propofol_titles = [('identifier',r'^\S+$'), ('sex',r'^[mf]$'), ('age', r'^\d{2}$'), ('weight(kg)', r'^\d{2,3}$'), ('height(cm)', r'^\d{3}$'),
 ('alcohol', r'^\d{1,2}$'), ('ihd', r'^[yn]$'), ('hypertension', r'^[yn]$'), ('sleep apnoea',r'^[yn]$'), ('diabetes', r'^[yn]$'),
  ('cvd', r'^[yn]$'), ('dementia', r'^[yn]$'), ('asa', r'^[1234]$'), ('procedure(p,c,d)', r'^[pcd]$'), ('start', r'^\d\d:\d\d$'), ('finish', r'^\d\d:\d\d$'),
   ('last dose time', r'^\d\d:\d\d$'), ('total dose(mg)', r'^\d{2,4}$'), ('n/v', r'^[yn]$'), ('pain', r'^[yn]$'), ('tolerating', r'^[yn]$'),
     ('ready for discharge', r'^[yn]$'), ('aldrete', r'^\d{1,2}$'),('time discharge assessment', r'^\d\d:\d\d$')]

def entry():
    with open('propofol_data.csv', 'ab') as csvfile:
        datawriter = csv.writer(csvfile, dialect='excel')
        while True:
            episode_data = []
            for data in propofol_titles:
                while True:
                    reply = raw_input(data[0] +':  ')
                    if re.search(data[1], reply):
                        episode_data.append(reply)
                        break
                    print '****** ?error ******'
            assert len(episode_data) ==  len(propofol_titles), 'There seems to be an error. ? missing data'
            datawriter.writerow(episode_data)
            response = raw_input('Add another episode? (y/n):  ')
            if response == 'n':
                print 'Exiting. Thanks!!'
                break

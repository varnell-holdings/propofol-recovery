import csv, re, click

# using 2.7 in conda env 'propofol'

prompts = [('patient/control', r'^[pc]$'),('identifier',r'^\S+$'), ('sex',r'^[mf]$'), ('age', r'^\d{2}$'), ('weight(kg)', r'^\d{2,3}$'), ('height(cm)', r'^\d{3}$'),
 ('alcohol', r'^\d{1,2}$'), ('ihd', r'^[yn]$'), ('hypertension', r'^[yn]$'), ('sleep apnoea',r'^[yn]$'), ('diabetes', r'^[yn]$'),
  ('cvd', r'^[yn]$'), ('dementia', r'^[yn]$'), ('asa', r'^[1234]$'), ('procedure(p,c,d)', r'^[pcd]$'), ('start (hh:mm)', r'^\d\d:\d\d$'), ('finish', r'^\d\d:\d\d$'),
   ('last dose time', r'^\d\d:\d\d$'), ('total dose(mg)', r'^\d{2,4}$'), ('n/v y/n', r'^[yn]$'), ('pain y/n', r'^[yn]$'), ('tolerating y/n', r'^[yn]$'),
     ('ready for discharge y/n', r'^[yn]$'), ('aldrete', r'^\d{1,2}$'),('time discharge assessment', r'^\d\d:\d\d$')]

def entry():
    with open('data.csv', 'ab') as csvfile:
        datawriter = csv.writer(csvfile, dialect='excel')
        while True:
            episode_data = []
            count = 0
            pat_cont = ''
            for data in prompts:
                while True:
                    reply = raw_input(data[0] +':  ')
                    if re.search(data[1], reply):
                        episode_data.append(reply)
                        count += 1
                        break
                    print '****** ?error ******'
                if count == 13 and episode_data[0] == 'c':
                    break
            datawriter.writerow(episode_data)
            response = raw_input('Add another episode? (y/n):  ')
            if response == 'n':
                print 'Exiting. Thanks!! *** Remember to git push origin master and upload to google **'
                break
if __name__ == '__main__':
    entry()

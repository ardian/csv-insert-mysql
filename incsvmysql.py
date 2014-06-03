import csv
import MySQLdb

mydb = MySQLdb.connect(host='',
    user='',
    passwd='',
    db='')
cursor = mydb.cursor()

csv_data = csv.reader(file('tabela.csv'))
for row in csv_data:

    cursor.execute('INSERT INTO tablename(produkti, \
          sasia, qmimi )' \
          'VALUES("%s", "%s", "%s")', 
          row)
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"

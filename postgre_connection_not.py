import psycopg2
from psycopg2.extras import DictCursor

try :
    connection = psycopg2.connect (
    host = 'localhost',
    user = 'postgres',
    password = 'maret082004asb',
    dbname = 'polban'
)

cursor = connection.cursor(cursor_factory=DictCursor)

#cursor.execute("INSERT INTO mahasiswa (nim,nama,nomor_hp) VALUES (221331064, 'Zuned', 6245632158955)")
#connection.commit()

cursor.execute ("SELECT nim, nama FROM mahasiswa")
data = cursor.fetchall()

for row in data :
    print(dict(row)['nama'])

except(Exception, psycopg2.KeyError) as error:
    print("Error")

finally :
if connection:
cursor.close()
connection.close()
print("PostgresSQL connection closed")
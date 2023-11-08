#my_tuple = (1, 'polban', 3.14)
#my_tuple[0] = 2
#print(my_tuple[0])

#my_dict = {
#    "nama" : "Arham",
#    "gender" : "L",
#    "NIM" : 221331035
#}
#print(my_dict)

#my_dict ['nama'] = 'tamara'
#my_dict['gender'] = 'P'
#my_dict['NIM'] = 221331077
#print(my_dict)


import psycopg2

connection = psycopg2.connect (
    host = 'localhost',
    user = 'postgres',
    password = 'maret082004asb',
    dbname = 'polban'
)

cursor = connection.cursor()
cursor.execute("INSERT INTO mahasiswa (nim,nama,nomor_hp) VALUES (221331064, 'Zuned', 6245632158955)")
connection.commit()
cursor.execute ("SELECT nim, nama FROM mahasiswa")
data = cursor.fetchall()

for row in data :
    print(row)

cursor.close()
connection.close()


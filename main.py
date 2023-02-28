import sqlite3


conn = sqlite3.connect('Artistc.db')

cursor = conn.cursor()
# cursor.execute('Select * from artists')
# results = cursor.fetchall()
# for result in results:
#     print(result)
# print(len(results))

# cursor.execute("insert into artists values (579, 'Ivan Kramskoi', 'Russian', 'Male', 1837)")
cursor.execute('Select * from artists')
results = cursor.fetchall()
for result in results:
    print(result)

# cursor.execute("Delete from artists where 'Id'=579")
# conn.commit()


conn.close()
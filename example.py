import sqlite3

# Establish connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# query data
cursor.execute("SELECT * from events WHERE Band='Lions'")
rows = cursor.fetchall()
# returns list of tuples as rows
print(rows)

cursor.execute("SELECT band, date from events WHERE Band='Lions'")
rows2 = cursor.fetchall()
print(rows2)

# insert new rows
rows3 = [('Dogs', 'Dog City', '2088.10.18'),
         ('Cats', 'Cat City', '2088.10.19')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", rows3)
connection.commit()

cursor.execute("SELECT * from events")
rows4 = cursor.fetchall()
print(rows4)

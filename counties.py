import sqlite3

# create a connection object
conn = sqlite3.connect('population.db')

# create a cursor object to interact with the database
cursor = conn.cursor()

counties = cursor.execute("SELECT DISTINCT county FROM population")
print(counties)
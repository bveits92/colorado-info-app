import sqlite3
import csv

conn = sqlite3.connect('population.db')

def create_table():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS population (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        county TEXT NOT NULL,
        year INTEGER NOT NULL,
        male INTEGER NOT NULL,
        female INTEGER NOT NULL,
        total INTEGER NOT NULL
    )''')
    conn.commit()

    with open('Colorado_population.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            c.execute('''INSERT INTO population (county, year, male, female, total) VALUES (?,?,?,?,?)''', (row[1], row[3], row[5], row[6], row[7]))
            conn.commit()

    conn.close()

create_table()

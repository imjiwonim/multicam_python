import csv
import pymysql

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'my_db'
}

# Connect to the database
conn = pymysql.connect(**config)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS TopGainerStockList(
        no int not null PRIMARY KEY,
        name VARCHAR(255),
        percent_change VARCHAR(255),
        last_price VARCHAR(20),
        high_price VARCHAR(20),
        low_price VARCHAR(20),
        volume VARCHAR(20)
        )
''')

# Read data from CSV and insert into table
with open('TopGainerStockList.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        no, name, percent_change, last_price, high_price, low_price, volume = row  # Adjust indices based on CSV
        percent_change = percent_change +'%'
        # cursor.execute('''
        #     INSERT INTO TopGainerStockList(no, name, percent_change, last_price, high_price, low_price, volume)
        #     VALUES (%s, %s, %s, %s, %s, %s, %s)
        # ''', (no, name, percent_change, last_price, high_price, low_price, volume))

conn.commit()
cursor.close()
conn.close()
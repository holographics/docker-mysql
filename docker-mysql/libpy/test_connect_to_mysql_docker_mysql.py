
# reference: https://www.w3schools.com/python/python_mysql_insert.asp

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="wpuser",
    port=3333,
    passwd="wpuser@",
    database="mysql"
)
print('...mydb %s %s' % (mydb, type(mydb)) )

mycursor = mydb.cursor(buffered=True)
print('...mycursor %s %s' % (mycursor, type(mycursor)) )

db_name = 'my_database5'

mycursor.execute("DROP DATABASE IF EXISTS %s" % db_name)

mycursor.execute("SHOW DATABASES")
for each in mycursor:
    print('... database %s' % each[0] )
    if each[0] == db_name:
        check = True
        break
else:
    check = False  

if check:
    print("...about to drop database %s" % db_name)
    mycursor.execute("DROP DATABASE %s" % db_name)
    print("...dropped database %s" % db_name)


mycursor.execute("CREATE DATABASE %s" % db_name)
print("...created database %s" % db_name)

mycursor.execute("USE %s" % db_name)


mycursor.execute("CREATE TABLE customers (name VARCHAR(255), fav INT(4), address VARCHAR(255))")
print("...created table customers %s" % db_name)

mycursor.execute("CREATE TABLE products (name VARCHAR(255), id INT(4))")
print("...created table products %s" % db_name)


# Insert Single Raw Into Table and Get Inserted ID
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print("...inserted customer %s into table customers" % str(val))
print("1 record inserted, ID:", mycursor.lastrowid)


# Insert Multiple Rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")



# Select From a Table 
mycursor.execute("SELECT * FROM customers")
print('...mycursor %s %s' % (mycursor, type(mycursor)) )

# All Rows
fetchall = mycursor.fetchall() # fetches all rows from the last executed statement.

print('... fetchall %s %s' % (fetchall, type(fetchall)) )
for each in fetchall:
    print('...each customer %s %s' % (each, type(each)) )

# One Row
mycursor.execute("SELECT * FROM customers")
fetchone = mycursor.fetchone()
print('... fetchone %s %s' % (fetchone, type(fetchone)) )

# Select With a Filter
mycursor.execute("SELECT * FROM customers WHERE address ='Park Lane 38'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# Wildcard Characters
mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


# Prevent SQL Injection
# Escape query values by using the placholder %s method
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)

myresult = mycursor.fetchall()
for x in myresult:
  print(x)


# Sort the Result
mycursor.execute("SELECT * FROM customers ORDER BY name DESC")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Delete Record
mycursor.execute("DELETE FROM customers WHERE address = 'Mountain 21'")
mydb.commit()

# Update Table
mycursor.execute("UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'")
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
# Update Table and Prevent SQL Injection
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()

# Limit the Result. return five records, starting from the third record
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Join Two or More Tables
sql = "SELECT customers.name AS user, products.name AS favorite FROM customers INNER JOIN products ON customers.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# Delete a Table
mycursor.execute("DROP TABLE customers")

# Drop Only if Exist
mycursor.execute("DROP TABLE IF EXISTS customers")





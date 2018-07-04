# First import sqlite3 library
# Then use .connect method for connection with data base
# Use .execute method for execute some task and query.
# USe .cursor method for data access inside the table  .
# And then close() both db and cursor .
import sqlite3
db=sqlite3.connect("gets.sqlite")
db.execute(" create table if not exists data (id integer, name text,age integer)")
db.execute(" insert into data values(001,'narsi',20)")
db.execute(" insert into data values(002,'jeetu',19)")

cursor=db.cursor()
cursor.execute("select * from data")
for id,name,age in cursor:
    print(id)
    print(name)
    print(age)
    print("-"* 20)
cursor.close()
db.close()

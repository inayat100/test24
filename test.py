
from psycopg2 import connect
conn = connect(
   database="python_db", user='inayat', password='inayat', host='localhost', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()


# cursor.execute("CREATE database python_db")
# cursor.execute('''CREATE TABLE Persons (
#     PersonID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );''')

# cursor.execute('''INSERT INTO persons
# VALUES ('4','khan','neha','muradabad','agra')''')
cursor.execute("select * from student")
for i in cursor.fetchall():
   print(f'''Id {i[0]} - Name {i[1]}   -  Age {i[2]}   - Gender  {i[3]} - City {i[4]}''')

print("=======crate==============")
# print("==",cursor.fetchall())


conn.close()

import mysql.connector

into_to_database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "962!%628E=EiM}Rgkap",
    database = "intro_to_database"
)

print(into_to_database.server_info)

mycursor = into_to_database.cursor()
mycursor.execute(""" 
CREATE TABLE IF NOT EXISTS Customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
)
 """)

print("Table created successfully")

# sql = "INSERT INTO Students (Student_ID,FirstName, LastName, Email, EnrollmentDate) VALUES (%s, %s, %s, %s, %s)"
# val = (6,"Bridget", "Boateng", "bridget@gmail.com", "2023-01-01")
# mycursor.execute(sql, val)
# into_to_database.commit()

# val = (7,"Samuel", "Boateng", "sam@gmail.com", "2023-01-01")
# mycursor.execute(sql, val)
# into_to_database.commit()

# val = (8,"Shadrach", "Agyekum", "agye@gmail.com", "2023-01-01")
# mycursor.execute(sql, val)
# into_to_database.commit()

# val = (9,"Prince", "Osei", "atta1@gmail.com", "2023-01-01")
# mycursor.execute(sql, val)
# into_to_database.commit()

# print(mycursor.rowcount,"record(s) inserted")

# Read All Customer Data
mycursor.execute("SELECT * from Students")
myresult = mycursor.fetchall()

print("Students:")
for row in myresult:
    print(row)
    
# update a student's email
sql = "UPDATE Students SET Email = %s WHERE Student_ID = %s"
val = ("samuel@gmail.com", 7)

mycursor.execute(sql,val)
into_to_database.commit()

print(mycursor.rowcount, "record(s) updated")

# Read the updated student data
mycursor.execute("SELECT * FROM Students WHERE Student_ID = 7")
myresult = mycursor.fetchone()

print("Updated Student: \n")
print(myresult)

# Delete a student
sql = "DELETE FROM Students WHERE Student_ID = 9"
mycursor.execute(sql)
into_to_database.commit()

print(mycursor.rowcount, "record(s) deleted.")

# close daabase connections
mycursor.close()
into_to_database.close()

print("Database connection closed")
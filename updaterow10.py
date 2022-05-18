import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Jessa Mae\Documents\Database1.accdb;')
    print("Database is Connected")

    Fullname = "Jessa Mae D. Mendoza"
    Age = "19"
    Course = "BSCPE"
    Address = "Cavite"
    Grade = "95"
    user_id = 10

    database = connection.cursor()
    database.execute('UPDATE Table1 SET Fullname=? Age=? Course=? Address=? Grade=? WHERE id=?',(Fullname,Age,Course,Address,Grade,user_id))
    connection.commit()

    print("Database is updated")

except pyodbc.Error:
    print("Database is NOT connected")
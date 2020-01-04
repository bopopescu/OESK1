import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="oeskdb"
)
mycursor = mydb.cursor()

def createDBMySQL():
  mycursor.execute("CREATE DATABASE oeskdb")
  mycursor.execute("CREATE TABLE people (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), age INTEGER)")

def insertMySQL():
    sql = "INSERT INTO people (firstname, lastname, age) VALUES (%s, %s, %s)"
    val = [
        ('Peter', 'Lowstreet', 20),
        ('Amy', 'Apple', 23),
        ('Hannah', 'Mountain', 21),
        ('Michael', 'Valley', 33),
        ('Sandy', 'Ocean', 44),
        ('Betty', 'Green', 32),
        ('Richard', 'Sky', 22),
        ('Susan', 'Sunday', 54),
        ('Vicky', 'Yellow', 32),
        ('Ben', 'Parker', 22),
        ('William', 'Central', 22),
        ('Chuck', 'Mallord', 24),
        ('Viola', 'Sideway', 33)
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")

def selectMySQL():
    sql = "SELECT * FROM people WHERE age = 33"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def updateMySQL():
    sql = "UPDATE people SET age = 44 WHERE age = 33"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) updated")

def deleteMySQL():
    sql = "DELETE FROM people WHERE age = 33"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

def main():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

if __name__ == "__main__":
    #main()
    #createDBMySQL()
    #insertMySQL()
    selectMySQL()
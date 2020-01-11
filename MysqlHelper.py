import mysql.connector
from timing import timing

class MysqlHelper:
    def __init__(self):
        self.cnx = mysql.connector.connect(
          host="localhost",
          user="root",
          passwd="password",
          database="oeskdb"
        )
        self.cursor = self.cnx.cursor()

    def createDB(self):
        #self.cursor.execute("CREATE DATABASE oeskdb")
        self.cursor.execute("CREATE TABLE people (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), weight INTEGER)")

    @timing
    def insert(self, data):
        sql = "INSERT INTO people (firstname, lastname, weight) VALUES (%s, %s, %s)"

        self.cursor.executemany(sql, data)
        self.cnx.commit()
        print(self.cursor.rowcount, "record(s) inserted")

    @timing
    def select(self):
        sql = "SELECT * FROM people WHERE weight = 55"
        self.cursor.execute(sql)
        self.cursor.fetchall()
        print(self.cursor.rowcount, "record(s) selected")

    @timing
    def update(self):
        sql = "UPDATE people SET weight = 66 WHERE weight = 64"
        self.cursor.execute(sql)
        self.cnx.commit()
        print(self.cursor.rowcount, "record(s) updated")

    @timing
    def delete(self):
        sql = "DELETE FROM people WHERE weight = 44"
        self.cursor.execute(sql)
        self.cnx.commit()
        print(self.cursor.rowcount, "record(s) deleted")


    def clear(self):
        sql = "DROP TABLE IF EXISTS people"
        self.cursor.execute(sql)

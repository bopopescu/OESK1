import mysql.connector
import csv
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
        self.cursor.execute("CREATE TABLE people (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), age INTEGER)")

    @timing
    def insert(self, data):
        sql = "INSERT INTO people (firstname, lastname, age) VALUES (%s, %s, %s)"
        '''val = [
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
        ]'''
        self.cursor.executemany(sql, data)
        self.cnx.commit()
        print(self.cursor.rowcount, "was inserted.")

    @timing
    def select(self):
        sql = "SELECT * FROM people WHERE age = 33"
        self.cursor.execute(sql)
        myresult = self.cursor.fetchall()
        for x in myresult:
            print(x)

    @timing
    def update(self):
        sql = "UPDATE people SET age = 44 WHERE age = 33"
        self.cursor.execute(sql)
        self.cnx.commit()
        print(self.cursor.rowcount, "record(s) updated")

    @timing
    def delete(self):
        sql = "DELETE FROM people WHERE age = 33"
        self.cursor.execute(sql)
        self.cnx.commit()
        print(self.cursor.rowcount, "record(s) deleted")


    def clear(self):
        sql = "DROP TABLE IF EXISTS people"
        self.cursor.execute(sql)

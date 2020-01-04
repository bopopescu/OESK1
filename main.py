import mysql.connector
import pymongo

##MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="oeskdb"
)
mycursor = mydb.cursor()


##MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["oeskdb"]
mycol = mydb["people"]


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

def clearMySQL():
    sql = "DROP TABLE IF EXISTS customers"
    mycursor.execute(sql)

def insertMongo():
    mylist = [
        {"firstname": "Peter", "lastname": "Lowstreet", "age": "20"},
        {"firstname": "Amy", "lastname": "Apple", "age": "23"},
        {"firstname": "Hannah", "lastname": "Mountain", "age": "21"},
        {"firstname": "Michael", "lastname": "Valley", "age": "33"},
        {"firstname": "Sandy", "lastname": "Ocean", "age": "44"},
        {"firstname": "Betty", "lastname": "Green", "age": "32"},
        {"firstname": "Richard", "lastname": "Sky", "age": "22"},
        {"firstname": "Susan", "lastname": "Sunday", "age": "54"},
        {"firstname": "Vicky", "lastname": "Yellow", "age": "32"},
        {"firstname": "Ben", "lastname": "Parker", "age": "22"},
        {"firstname": "William", "lastname": "Central","age": "22"},
        {"firstname": "Chuck", "lastname": "Mallord", "age": "24"},
        {"firstname": "Viola", "lastname": "Sideway", "age": "33"}
    ]
    x = mycol.insert_many(mylist)
    print(x.inserted_ids)

def selectMongo():
    myquery = {"age": "33"}
    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)

def updateMongo():
    myquery = {"age": "33"}
    newvalues = {"$set": {"age": "33"}}

    mycol.update_one(myquery, newvalues)
    for x in mycol.find():
        print(x)

def deleteMongo():
    myquery =  {"age": "33"}

    x = mycol.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")

def clearMongo():
    mycol.drop()

def main():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

if __name__ == "__main__":
    #main()
    #createDBMySQL()
    #insertMySQL()
    #selectMySQL()
    #updateMySQL()
    #deleteMySQL()
    #insertMongo()
    selectMongo()
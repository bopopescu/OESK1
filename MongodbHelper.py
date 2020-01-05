import pymongo
from timing import timing
import pandas as pd

class MongodbHelper:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["oeskdb"]
        self.col = self.db["people"]

    def csv_to_json(filename):
        data = pd.read_csv(filename, sep=';', header=None)
        return data.to_dict('records')

    @timing
    def insert(self):
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
            {"firstname": "William", "lastname": "Central", "age": "22"},
            {"firstname": "Chuck", "lastname": "Mallord", "age": "24"},
            {"firstname": "Viola", "lastname": "Sideway", "age": "33"}
        ]
        x = self.col.insert_many(mylist)
        # print(x.inserted_ids)

    @timing
    def select(self):
        myquery = {"age": "33"}
        mydoc = self.col.find(myquery)

        # for x in mydoc:
        #    print(x)

    @timing
    def update(self):
        myquery = {"age": "33"}
        newvalues = {"$set": {"age": "44"}}

        x = self.col.update_many(myquery, newvalues)

        print(x.modified_count, "documents updated.")

    @timing
    def delete(self):
        myquery = {"age": "33"}

        x = self.col.delete_many(myquery)
        print(x.deleted_count, "documents deleted.")

    def clear(self):
        self.col.drop()

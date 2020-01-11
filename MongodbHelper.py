import pymongo
from timing import timing

class MongodbHelper:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["oeskdb"]
        self.col = self.db["people"]

    def dataPrepare(self, data):
        res = []
        for row in data:
            json_row = {}
            json_row['firstname'] = row[0]
            json_row['lastname'] = row[1]
            json_row['weight'] = int(row[2])
            res.append(json_row)
        return res

    @timing
    def insert(self, data):
        x = self.col.insert_many(data)
        print(len(x.inserted_ids), "documents inserted.")

    @timing
    def select(self):
        myquery = {"weight": 55}
        x = self.col.find(myquery)
        print(x.count(), "documents selected.")

    @timing
    def update(self):
        myquery = {"weight": 64}
        newvalues = {"$set": {"weight": 66}}
        x = self.col.update_many(myquery, newvalues)
        print(x.modified_count, "documents updated.")

    @timing
    def delete(self):
        myquery = {"weight": 44}
        x = self.col.delete_many(myquery)
        print(x.deleted_count, "documents deleted.")

    def clear(self):
        self.col.drop()

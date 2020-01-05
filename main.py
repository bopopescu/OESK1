from MysqlHelper import MysqlHelper
from MongodbHelper import MongodbHelper

import csv

if __name__ == "__main__":
    with open('file2.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile, delimiter=';'))

    mysql_helper = MysqlHelper()

    mysql_helper.createDB()
    mysql_helper.insert(data)
    mysql_helper.select()
    mysql_helper.update()
    mysql_helper.delete()
    mysql_helper.clear()


    mongodb_helper = MongodbHelper()

    json_data = mongodb_helper.dataPrepare(data)

    mongodb_helper.insert(json_data)
    mongodb_helper.select()
    mongodb_helper.update()
    mongodb_helper.delete()
    mongodb_helper.clear()

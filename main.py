from MysqlHelper import MysqlHelper
from MongodbHelper import MongodbHelper

if __name__ == "__main__":
    mysql_helper = MysqlHelper()

    mysql_helper.createDB()
    mysql_helper.insert()
    mysql_helper.select()
    mysql_helper.update()
    mysql_helper.delete()
    mysql_helper.clear()


    mongodb_helper = MongodbHelper()

    mongodb_helper.insert()
    mongodb_helper.select()
    mongodb_helper.update()
    mongodb_helper.delete()
    mongodb_helper.clear()

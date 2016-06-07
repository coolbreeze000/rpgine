from pymongo import MongoClient

class DBHandler:
    def __init__(self, ip, port):
        self.db_conn = MongoClient("mongodb://{}:{}".format(ip,port))

    def getConnection(self):
        return self.db_conn

from uuid import uuid1
import hashlib

class GenericDatabaseObject:
    def __init__(self,name):
        self.uuid = uuid1()
        self.name = name

from uuid import uuid5, NAMESPACE_DNS
import hashlib

class GenericDatabaseObject:
    def __init__(self,name):
        self.uuid = uuid5(NAMESPACE_DNS, name)
        self.name = name
        print(self.uuid)

# Just for testing
GenericDatabaseObject("name")
from PersistenceAPI import DBHandler

driver = DBHandler("192.168.99.100","27017").getConnection()
db = driver["test_db"]
db["test_collection"].insert_one({"asd":"asd"})
result = db["test_collection"].find()
for x in result:
    print(x)

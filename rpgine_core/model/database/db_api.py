from pymongo import MongoClient

driver = MongoClient("mongodb://192.168.99.100:27017")
db = driver["test_db"]
result = db.restaurants.insert_one({"asd":"fgh"})

from PersistenceAPI import DBHandler

driver = DBHandler("192.168.99.100","27017").getConnection()
db = driver["Dance_of_Dragons_RPG_DB"]
db["characters"].insert_one({
    "player_characters": [{
        "nelia": [{
            "properties": [{
                "display_name": "Nelia Himmelsstein"}, {
                "attributes": [{
                    "strength": [{
                        "display_name": "Strength"}, {
                        "value": "3"}
                    ]}
                ]}
            ]}
        ]}
    ]}
)

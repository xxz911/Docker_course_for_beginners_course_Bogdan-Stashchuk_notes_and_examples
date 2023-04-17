from pymongo import MongoClient
from pprint import pprint

# mongo - имя другого сервиса
MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("listDatabases")
# Выводим в лог базы данных
pprint(dbs_list)

print("End")

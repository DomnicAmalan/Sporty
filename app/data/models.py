from pymongo import MongoClient
from app.config import DevelopmentConfig as DBconfig

client = MongoClient(DBconfig.Hostname, DBconfig.Port)
db = client[DBconfig.DB_NAME]
print(db)


from pymongo import MongoClient
from app.config import DevelopmentConfig as DBconfig

client = MongoClient(DBconfig.Hostname, DBconfig.DB_Port)
db = client[DBconfig.DB_NAME]

sports_list = db.sports_list
users = db.users
verication_codes = db.verification_system

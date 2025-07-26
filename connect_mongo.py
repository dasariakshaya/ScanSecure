import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["licenseDB"]
collection = db["registration_certificates"]

# Load the JSON file (use raw string r"" to avoid path issues)
json_path = r"C:\Users\AKSHAYA DASARI\Downloads\fake_rc_records_50000_full_random.json"
with open(json_path, "r") as f:
    data = json.load(f)

# Insert into MongoDB
collection.insert_many(data)

print("✅ Data inserted into MongoDB successfully")

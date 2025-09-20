"""
Title: Lutz_usersp1.py
Author: Melissa Lutz
Date: 19 September 2025
Description: Hands-On 4.2 - Python with MongoDB, Part I. Connects to web335DB and demonstrates basic read queries.
"""

# Import the MongoClient
import os
from pymongo import MongoClient
from pprint import pprint


FALLBACK_MONGO_URI = "mongodb+srv://web335Admin:s3cret@computer.3dociam.mongodb.net/web335DB?retryWrites=true&w=majority"

def get_client() -> MongoClient:
    uri = os.getenv("MONGO_URI", FALLBACK_MONGO_URI).strip()
    if "<your-cluster-host>" in uri:
        raise ValueError("Set MONGO_URI or replace <your-cluster-host> in FALLBACK_MONGO_URI.")
    return MongoClient(uri, serverSelectionTimeoutMS=10000)

def main():
    client = get_client()
    db = client["web335DB"]
    print("Connected to MongoDB:", client)

    # 4. Display all documents in the users collection (projection: first and last names only)
    print("\nAll users (first & last names):")
    for user in db.users.find({}, {"_id": 0, "firstName": 1, "lastName": 1}):
        print(user)

    # 5. Display a document where employeeId is 1011
    print("\nUser with employeeId == '1011':")
    doc_emp = db.users.find_one({"employeeId": "1011"})
    pprint(doc_emp)

    # 6. Display a document where lastName is Mozart
    print("\nUser with lastName == 'Mozart':")
    doc_ln = db.users.find_one({"lastName": "Mozart"})
    pprint(doc_ln)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)

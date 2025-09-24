"""
Title: Lutz_usersp2.py
Author: Melissa Lutz
Date: 23 September 2025
Description: Hands-On 5.2 - Python with MongoDB, Part II.
             Connects to web335DB and performs CRUD with printed proof.
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint
from datetime import datetime, timezone

uri = "mongodb+srv://web335_user:s3cret@computer.3dociam.mongodb.net/?retryWrites=true&w=majority&appName=Computer"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# --- CRUD helpers ---
def create_user(db, employee_id: str) -> None:
    user_doc = {
        "firstName": "MelissaTest",
        "lastName": "Lutz",
        "employeeId": employee_id,
        "email": "melissa.lutz@example.com",
        "dateCreated": datetime.now(timezone.utc),
    }
    inserted_id = db.users.insert_one(user_doc).inserted_id
    print(f"[CREATE] Inserted _id: {inserted_id}")

def prove_created(db, employee_id: str) -> None:
    doc = db.users.find_one({"employeeId": employee_id})
    print("[PROVE CREATE] Document:")
    pprint(doc)

def update_email(db, employee_id: str, new_email: str) -> None:
    result = db.users.update_one(
        {"employeeId": employee_id},
        {"$set": {"email": new_email, "dateUpdated": datetime.now(timezone.utc)}}
    )
    print(f"[UPDATE] matched: {result.matched_count}, modified: {result.modified_count}")

def prove_updated(db, employee_id: str) -> None:
    doc = db.users.find_one({"employeeId": employee_id})
    print("[PROVE UPDATE] Document:")
    pprint(doc)

def delete_user(db, employee_id: str) -> None:
    result = db.users.delete_one({"employeeId": employee_id})
    print(f"[DELETE] deleted: {result.deleted_count}")

def prove_deleted(db, employee_id: str) -> None:
    doc = db.users.find_one({"employeeId": employee_id})
    print("[PROVE DELETE] Document (should be None):", doc)

# --- Main ---
def main():
    employee_id = f"ml-{int(datetime.now(timezone.utc).timestamp())}"
    try:
        db = client["web335DB"]
        print("Connected to MongoDB. Using database:", db.name)
        print(f"Using employeeId: {employee_id}\n")

        create_user(db, employee_id)
        prove_created(db, employee_id)

        update_email(db, employee_id, "melissa.lutz+updated@example.com")
        prove_updated(db, employee_id)

        delete_user(db, employee_id)
        prove_deleted(db, employee_id)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

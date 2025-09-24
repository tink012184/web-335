"""
Title: Lutz_usersp1.py
Author: Melissa Lutz
Date: 23 September 2025
Description: Hands-On 4.2 - Python with MongoDB, Part I.
             Connects to web335DB and prints:
             1) all users
             2) the user with employeeId = 1011
             3) all users with lastName = 'Mozart'
"""


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://web335_user:s3cret@computer.3dociam.mongodb.net/?retryWrites=true&w=majority&appName=Computer"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def print_section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

def main() -> None:
    # 1) Ping + choose DB
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["web335DB"]

    # 2) Display ALL documents in users
    print_section("All user documents")
    try:
        for doc in db.users.find({}):
            pprint(doc)
    except Exception as e:
        print(f"[ERROR] Reading all users failed: {e}")

    # 3) Display document where employeeId = 1011
    print_section("User with employeeId = 1011")
    try:
        # Some datasets store employeeId as a string, some as a number—try both:
        user = db.users.find_one({"employeeId": "1011"}) or db.users.find_one({"employeeId": 1011})
        if user:
            pprint(user)
        else:
            print("No document found with employeeId 1011.")
    except Exception as e:
        print(f"[ERROR] Query by employeeId failed: {e}")

    # 4) Display document(s) where lastName = 'Mozart'
    print_section("Users with lastName = 'Mozart'")
    try:
        mozarts = list(db.users.find({"lastName": "Mozart"}))
        if mozarts:
            for m in mozarts:
                pprint(m)
        else:
            print("No documents found with lastName 'Mozart'.")
    except Exception as e:
        print(f"[ERROR] Query by lastName failed: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[FATAL] {e}")
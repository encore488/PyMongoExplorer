import os
import pprint
from pymongo import MongoClient

# Connect to the MongoDB server and find database names
connection_string = "mongodb+srv://datasense68:aB4j11JSG4AdCw0W@firstcluster.b1klogf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
dbs = client.list_database_names()

# Print the collections in 'test' database
test_db = client.test
test_collections = test_db.list_collection_names()
#print(test_collections)

users = client.users
user_collection = users.user_collection

def insert_new_user (name, email, password, hiscore = 0, level = 0, experience = 0):
    # Insert a document into the user collection
    user_doc = {"name": name, "email": email, "password": password, "hiscore": hiscore, "level": level, "experience": experience}
    user_collection.insert_one(user_doc)

    # Print the inserted document
    pprint.pprint(user_collection.find_one())
    
insert_new_user("Lori", "katLady45@hotmail.com", "password456")
    
# Insert multiple documents into a collection
def create_documents():
    goal_names = ["Get Strong", "Complete House", "Learn Python", "Learn Computer Vision", "Apply for Internships"]
    deadlines = ["2024-12-31", "2025-12-31", "2024-04-01", "2025-12-31", "2024-06-31"]
    methods = ["Lift and Sprint", "Construction", "Make games, Leetcode, and attend Hackathons", "Free courses + spinoffs", "Average 1 application a day"]
    descriptions = ["Lift 3-4 days a week, or calisthenics if you can't. Warm up to a sprint at least once a week.",
                    "Take responsibility for more house stuff. Initiate projects. Don't wait.", 
                    "Get to medium level Leetcodes without assistance. Then Django, Pygame, MongoDB mix.",
                   "Free courses (1 or 2), then Kaggle like you're mad!", "Apply to 1-2 internships a day. Don't wait."]
    for i in range(len(goal_names)):
        goal_collection.insert_one({"name": goal_names[i], "deadline": deadlines[i], "method": methods[i], "description": descriptions[i]})
        

def find_all_documents():
    # Find all documents in the collection
    for doc in user_collection.find():
        pprint.pprint(doc)
        
#find_all_documents()

def find_one_document():
    # Find one document in the collection
    pprint.pprint(user_collection.find_one({"name": "Lori"}))
    
def count_documents():
    # Count the number of documents in the collection
    count = user_collection.count_documents(filter={})
    print("Number of users: ", count)
    
count_documents()

def get_user_by_id(userId):
    from bson.objectid import ObjectId
    _id = ObjectId(userId)
    user = user_collection.find_one({"_id": _id})
    pprint(user)
    
def get_level_range(min_level, max_level):
    for user in user_collection.find({"level": {"$gte": min_level, "$lte": max_level}}):
        pprint(user)
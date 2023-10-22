import os
import pprint
from pymongo import MongoClient

# Connect to the MongoDB server and find database names
connection_string = "mongodb+srv://datasense68:aB4j11JSG4AdCw0W@firstcluster.b1klogf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
dbs = client.list_database_names()

# Create db and print the collections in 'test' database (just as an exercise)
test_db = client.test
test_collections = test_db.list_collection_names()
#print(test_collections)

# Create the gameDB and a collection for the users
gameDB = client.gameDB
user_collection = gameDB.user_collection


def insert_new_user (name, email, password, hiscore = 0, level = 0, experience = 0):
    # Insert a document into the user collection
    user_doc = {"name": name, "email": email, "password": password, "hiscore": hiscore, "level": level, "experience": experience}
    user_collection.insert_one(user_doc)

    # Print the inserted document
    pprint.pprint(user_collection.find_one())
    
#insert_new_user("Lori", "katLady45@hotmail.com", "password456")
    
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


# Insert multiple documents into a collection
def populate_users():
    names = ["xXxJasonxXx", "Kylie99", "Adrian's Revenge", "BubleGum", "BigBoy", "Blastoise", "Charizard", "Squirtle", "Pikachu", "Bulbasaur"]
    emails = ["jjPreston@yahoo.com", "KkMcNeal99@gmail.com", "LittleShow5@hotlink.net", "MichaelsNewEmail@gmail.com", "Frisch555@fartmail.gov", "butWhy?@yahoo.com", "FireBreather21@gmail.com", "inappropriateStuff77@yahoo.com", "pikaPika@pika.com", "bulby12456@poketMonsters.net"]
    passwords = ["password123", "password456", "password789", "password101", "password112", "password131", "password415", "password161", "password718", "password919"]
    hiscores = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    levels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    experiences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    
    for i in range(len(names)):
        user_collection.insert_one({"name": names[i], "email": emails[i], "password": passwords[i], "hiscore": hiscores[i], "level": levels[i], "experience": experiences[i]})
        


def find_all_documents():
    # Find all documents in the collection
    for doc in user_collection.find():
        pprint.pprint(doc)
        

def find_one_document():
    # Find one document in the collection
    pprint.pprint(user_collection.find_one({"name": "Lori"}))
    

def count_documents():
    # Count the number of documents in the collection
    count = user_collection.count_documents(filter={})
    print("Number of users: ", count)
    

def get_user_by_id(userId):
    from bson.objectid import ObjectId
    _id = ObjectId(userId)
    user = user_collection.find_one({"_id": _id})
    pprint(user)
    

def get_level_range(min_level, max_level):
    query =         {"$and": [
            {"level": {"$gte": min_level}},
            {"level": {"$lte": max_level}}
            ]}
    people = user_collection.find(query).sort("level")
    for person in people:
        pprint.pprint(person)


def project_columns():
    columns = {"_id": 0, "name": 1, "email": 1}
    people = user_collection.find({}, columns)
    for person in people:
        pprint.PrettyPrinter(indent=4).pprint(person)
        

def update_user(user_id):
    from bson.objectid import ObjectId
    _id = ObjectId(user_id)
    all_updates = {
        "$set": {"beginner": False},
        "$inc": {"experience": 1000},
        "$rename": {"hiscore": "highscore"}
        }
    user_collection.update_one({"_id": _id}, all_updates)
    
def replace_one(user_id):
    from bson.objectid import ObjectId
    _id = ObjectId(user_id)
    new_doc = {"name": "Lori", "email": "highFlyer79@elitist.gov",
               "password": "IgJks6*83bU8eK)3Y", "hiscore": 12089, "level": 19, "experience": 0}
    user_collection.replace_one({"_id": _id}, new_doc)
    
def delete_one(user_id):
    from bson.objectid import ObjectId
    _id = ObjectId(user_id)
    user_collection.delete_one({"_id": _id})
    

ship1 = {"name": "Little Yellow", "health": 100, "damage": 20, "speed": 10, "healRate": 5, "terraformRate": 5, "special": "None", "price": 0, "_id": "5f9b7b7b9c9a9b9c9a9b9c9a"}
ship2 = {"name": "Big Blue", "health": 200, "damage": 10, "speed": 7, "healRate": 10, "terraformRate": 10, "special": "Bolt", "price": 500, "_id": "5f9b7b7b9c9a9b9c9a9b9c9b"}
ship3 = {"name": "Green Machine", "health": 150, "damage": 20, "speed": 12, "healRate": 5, "terraformRate": 5, "special": "Machine Gun", "price": 1000, "_id": "5f9b7b7b9c9a9b9c9a9b9c9c"}
ship4 = {"name": "Grey Ghost", "health": 65, "damage": 15, "speed": 20, "healRate": 10, "terraformRate": 5, "special": "Buddy", "price": 2500, "_id": "5f9b7b7b9c9a9b9c9a9b9c9d"}
ship5 = {"name": "Big Yellow", "health": 300, "damage": 25, "speed": 7, "healRate": 5, "terraformRate": 15, "special": "Storm", "price": 8000, "_id": "5f9b7b7b9c9a9b9c9a9b9c9e"}
ship6 = {"name": "Little Blue", "health": 100, "damage": 15, "speed": 15, "healRate": 20, "terraformRate": 20, "special": "Grapeshot", "price": 10000, "_id": "5f9b7b7b9c9a9b9c9a9b9c9f"}
ship7 = {"name": "UFO", "health": 100, "damage": 30, "speed": 30, "healRate": 5, "terraformRate": 5, "special": "Laser", "price": 20000, "_id": "5f9b7b7b9c9a9b9c9a9b9c10"}

def add_ship_embed(user_id, ship):
    from bson.objectid import ObjectId
    _id = ObjectId(user_id)
    user_collection.update_one({"_id": _id}, {"$addToSet": {'ships': ship}})
    
#add_ship_embed("5f9b7b7b9c9a9b9c9a9b9c9a", ship1)

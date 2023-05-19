from pymongo import MongoClient


client = MongoClient('mongodb://localhost:32768')
db = client['mydatabase']
collection = db['mycollection']

# Insert a document into the collection
post = {'title': 'My first blog post!', 'content': 'Hello world!'}
collection.insert_one(post)

collection.bulk_write([
    insert_one:{_id:3, type:"Nani"},
    insert_one:{_id:4,type:"poorl"}
    ])


# Query the collection
for post in collection.find():
    print(post)

from pymongo import MongoClient



client = MongoClient("mongodb+srv://taapas:<password>@cluster0.euh9t.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.todo_app

collection_name = db["todos_app"]

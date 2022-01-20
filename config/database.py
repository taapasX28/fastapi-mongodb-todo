from pymongo import MongoClient
from kafka import KafkaConsumer
from kafka import KafkaProducer
import json

client = MongoClient("mongodb+srv://Taapas:taapas@cluster0.kpoyr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
consumer = KafkaConsumer('todo1', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=True, group_id='my-group' ,value_deserializer=lambda x: json.loads(x.decode('utf-8')))

db = client.todo_app

collection_name = db["todos_app"]

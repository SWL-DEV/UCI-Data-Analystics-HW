from flask import Flask, render_template

# Import pymongo library to connect the Flask app to Mongo database
import pymongo

# Create an instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance
client = pymongo.MongoClient(conn)

# Connect to Mars News Database. Create one if not already available
db = client.mars_db

# Drop collection if available to remove duplicates
db.mars.drop()






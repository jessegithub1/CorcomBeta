# corDB.py

# https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<<MONGODB URL>>)
#db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
# https://stackoverflow.com/questions/22139173/how-to-connect-to-mongo-database-locally-using-python

#
#
# Note:  need to make sure mongodb is installed on computer -- on mac control click on icon in bin after install
# to OK use of downloaded application.
#


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'cor_db_1'
COLLECTION_NAME = 'c1'

client = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = client.DB_NAME
collection = db.COLLECTION_NAME 
collection.find_one({"name":"name1"})

serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
from pymongo import *
import pprint

def printResult(_cursor, _attribution=None):
    if(_attribution):
        for item in _cursor:
            pprint.pprint(item[_attribution])
        return
    for item in _cursor:
        pprint.pprint(item)

# Connect to mongodb
client = MongoClient("mongodb://localhost:27017/")
db = client.lagou
collection = db.lagouJob



# Find by company name
cursor = collection.find({"companyName":"通联数据股份公司"})

# Find by Job Title
cursor = collection.find({"jobTitle":{"$regex": u"区块"}})
printResult(cursor, "jobDescription")


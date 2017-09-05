# -*- encoding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
from pymongo import *
import pprint


nlp = BosonNLP('CIeQWQuR.15234.TVGB35Uq5nuk')





def decodeResult(_cursor, _attribution=None):
    results = []
    if(_attribution):
        for item in _cursor:
            results.append(item[_attribution])
            # pprint.pprint(item[_attribution])
        return results
    for item in _cursor:
        pprint.pprint(item)
    return

# Connect to mongodb
client = MongoClient("mongodb://localhost:27017/")
db = client.lagou
collection = db.lagouJob



# Find by company name
cursor = collection.find({"companyName":"深圳市贝利美维软件有限公司"})

# Find by Job Title
# cursor = collection.find({"jobTitle":{"$regex": u"区块链"}})
result = decodeResult(cursor, "jobDescription")
resultContent = "".join(result)
nlpResult = nlp.extract_keywords(resultContent, top_k=100)

f = open('companyKeywords.txt', 'w')
for weight, word in nlpResult:
    outString = str(weight) + " "+ str(word) + "\n"
    print(weight, word)
    f.write(outString)
f.close() 


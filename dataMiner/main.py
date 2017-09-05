import xlrd
import os, sys, inspect
import wizard
# from wizard import *
from pymongo import *



fileLocation = "./data.xls"
workBook = xlrd.open_workbook(fileLocation)

sheetsNum = workBook.nsheets
companySet = set()

for index in range(sheetsNum):
	print("============================\nSheet: ", index,"\n====================================")
	currentSheet = workBook.sheet_by_index(0)
	# print(workBook.sheet_by_index(0).nrows)
	rowNum = currentSheet.nrows
	colNum = currentSheet.ncols
	for indexRow in range(rowNum):
		companyName = currentSheet.cell_value(indexRow,0)
		if companyName == "企业名称":
			continue
		# print(companyName)
		companySet.add(companyName)

companyList = list(companySet)
# Connect to mongodb
client = MongoClient("mongodb://localhost:27017/")
db = client.lagou
collection = db.lagouJob

# Get the list for exist companies
existCompanyList = []
companyCursor = collection.distinct("companyName")
for _company in companyCursor:
	existCompanyList.append(_company)
# print(existCompanyList)

for company in companyList:
	if company in existCompanyList:
		print(company, "is collected already")
		continue
	currentCompanyJobList = []
	print("Getting postions of:", company)
	try:
		currentCompanyJobList = wizard.lagou.lagouMethod(company)
	except Exception as e:
		print(e)
	if len(currentCompanyJobList) == 0:
		print("No job found in", company)
		continue
	print("Get", len(currentCompanyJobList), "jobs, inserting to db")
	for job in currentCompanyJobList:
		jobObj = job.toJson()
		collection.insert_one(jobObj)

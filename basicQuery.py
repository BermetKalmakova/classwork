import pymongo

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.test 
collection = db.restaurants 

def searchBy_Borough(borough):
    for each in collection.find({"borough": borough}):
        print each

def searchBy_Zipcode(zipcode):
    for each in collection.find({"address.zipcode": zipcode}):
        print each

def searchBy_Zip_Grade(zipcode, grade):
    for each in collection.find({"address.zipcode": zipcode, "grades.grade": grade}):
        print each

def searchyBy_Zip_SmallerScore(zipcode,score):
    for each in collection.find({"address.zipcode": zipcode, "grades.score": {"$lt": score}}):
        print each

def searchBy_Zip_Cuisine_GreaterScore(zipcode,cuisine,score):
    for each in collection.find({"address.zipcode": zipcode, "cuisine": cuisine, "grades.score": {"$gt": score}}):
        print each

searchBy_Borough("Brooklyn")
searchBy_Zipcode("11212")
searchBy_Zip_Grade("11212","B")
searchyBy_Zip_SmallerScore("11212", 4)
searchBy_Zip_Cuisine_GreaterScore("11212","Pizza",10)
## download link: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
##  American Movies Scrapped from America 

## JSON contains: title, year, director,cast, genre, and notes

##
## We imported by importing the json module
##  Then we open the json and used a variable to hold the json contents (this variable is a list)
##  Using insert_many we inserted everything in the list into the database. 
##
##

import pymongo, json
with open("movies.json", "r") as f:
    moviesList = json.load(f)

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection.leiGkalmakovaB 
collection = db.movies
collection.insert_many(moviesList) 


def queryTitle(title):
    for each in collection.find({"title": title}):
        print each

def queryYear(year):
    for each in collection.find({"year": year}):
        print each

def queryDirector(director):
    for each in collection.find({"director": director}):
        print each

def queryGenre(genre):
    for each in collection.find({"genre": genre}):
        print each

def queryInclusiveBetweenYears(y1,y2):
    for each in collection.find({"$and": [{"year":{"$lte": y2}}, {"year":{"$gte": y1}}]}):
        print each

queryTitle("After Dark in Central")
queryYear(1900)
queryDirector("James H. White")
queryGenre("Short")
queryInclusiveBetweenYears(1900,1902)

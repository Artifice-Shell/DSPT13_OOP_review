import pymongo

client = pymongo.MongoClient("mongodb://Admin:M0db0y1977@cluster0.lmqsp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

    conn = client
    col = db['myFirstDatabase']
    curs = client.cursor()
    curs.execute()
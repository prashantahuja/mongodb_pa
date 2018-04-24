from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['pymongo_test']
posts = db.posts

post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PMW',
    'author': 'Prashant'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Corporate Actions',
    'author': 'Prashant'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Reference Data',
    'author': 'Prashant'
}
post_4 = {
    'title': 'Learning Python',
    'content': 'Fales Elementary',
    'author': 'Varun'
}
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

cursor = db.posts.find({"$and":[{'author':"Prashant"},{'content':"PMW"}]})

for doc in cursor:
    print(doc)
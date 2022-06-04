import pymongo
client = pymongo.MongoClient("")

try:
    print(client.server_info())
except Exception:
    print("Unable to connect to the server.")

posts_db = client['sample_airbnb']
collection = posts_db['listingsAndReviews']
return_values = collection.aggregate(
    [
        {
            '$match': {
                'beds': {
                    '$gt': 2
                }
            }
        }, {
            '$sort': {
                'price': 1
            }
        }, {
            '$limit': 5
        }
    ]
)

for item in return_values:
    print(item)
print('===')



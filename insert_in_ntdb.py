import json
from pprint import pprint
import pymongo
client = pymongo.MongoClient("")

posts_db = client['nt_data']
collection = posts_db['stocks']
print(f'count: {collection.count_documents({})}')
f = open('new_sample.json')

json_data = json.load(f)
# print(json_data)

prefix_list = ['Adj_', 'Close_', 'High_', 'Low_', 'Open_', 'Volume_']
prefix_dict = {
    'Adj_': 'adj',
    'Close_': 'close',
    'High_': 'high',
    'Low_': 'low',
    'Open_': 'open',
    'Volume_': 'volume'
}
stocks_names_list = [
    'AAPL',
    'AMZN',
    'DIA',
    'FB',
    'GLD',
    'GOOG',
    'GOOGL',
    'GOVT',
    'IAU',
    'IEF',
    'IGSB',
    'IVV',
    'LQD',
    'MSFT',
    'NFLX',
    'QQQ',
    'SHY',
    'SPY',
    'TLT',
    'TSLA',
    'VCIT',
    'VCSH',
    'VIXY',
    'VOO',
]

"""
item: {
    time: index, 
    stock_name_1: {
        adj: _, open: _, high: _, low: _, close: _, volume: _} 
    },
    stock_name_2: { ... },
    stock_name_3: { ... },
    stock_name_4: { ... },
}
"""

# for i in range(len(json_data['index'])):
#     item = {'time': json_data['index'][i]}
#     for stock in stocks_names_list:
#         item[stock] = {}
#         for prefix in prefix_list:
#             name_of_column = f'{prefix}{stock}'
#             item[stock][prefix_dict[prefix]] = json_data[name_of_column][i]
#
#     print(f'\riteration: {i}', end='')
#     new_values = {"$set": item}
#
#     collection.update_one({'time': item['time']}, new_values, upsert=True)
all_files = collection.find({}, {'time': 1, 'AAPL': 1, '_id': 0})
# db.inventory.find( { status: "A" }, { item: 1, status: 1, _id: 0 } )
result_list = list(all_files)
pprint(result_list)

print('===')



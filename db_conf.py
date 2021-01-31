from db import *

payload = { "_type": "location",
			"acc": 68, 
			"alt": 0, 
			"batt": 78, 
			"bs": 2, 
			"conn": "w", 
			"created_at": 1611772063, 
			"lat": 8.2631383, 
			"lon": -62.7914465, 
			"t": "u", 
			"tid": "g4", 
			"tst": 1611772057, 
			"vac": 0, 
			"vel": 0
			}

a_list = next(db.fetch())

if len(a_list) == 0:
    print('detaBase is empty')
    print('Generating key')
    id_gen = db.insert(payload)
    print('Your id is: ')
    b_list = next(db.fetch())
    for items in b_list:
    	print(items['key'])

else:
	print('detaBase is setup')
	print('Your id is: ')
	for items in a_list:
		print(items['key'])
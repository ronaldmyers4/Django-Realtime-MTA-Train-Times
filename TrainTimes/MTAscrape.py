from google.transit import gtfs_realtime_pb2
import requests
import json
import pandas as pd
import threading

#class MTAscrape():
global response123456
global responseACE
global responseBDFM
global responseNQRW
global responseL
global responseG
global x

response123456 = None
responseACE = None
responseBDFM = None
responseNQRW = None
responseL = None
responseG = None
x = 0
		
#def __init__(self):
	#pass
	
"""
self.response123456 = None

self.responseACE = None

self.responseNQRW = None

self.responseBDFM = None

self.responseL = None

self.responseG = None
"""
	
def scrape():
	threading.Timer(15.0, scrape).start()	
	global response123456
	global responseACE
	global responseBDFM
	global responseNQRW
	global responseL
	global responseG
	global x
	
	x += 1
	
	response123456 = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=1')

	responseACE = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=26')

	responseNQRW = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=16')
	
	responseBDFM = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=21')

	responseL = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=2')
	
	responseG = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=31')
	
	print(response123456)

	return response123456, responseACE, responseBDFM, responseNQRW, responseL, responseG, x
		
scrape()
	
		

		
	
	
	
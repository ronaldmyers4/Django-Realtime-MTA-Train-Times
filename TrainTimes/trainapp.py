from TrainTimes import views
from google.transit import gtfs_realtime_pb2
import requests
import json
import time
import datetime
import pandas as pd
import schedule
import threading
from TrainTimes import MTAscrape


"""class MTAscrape(object):
	def __init__(self):
		self.scrape123456 = None
		self.scrapeACE = None
		self.scrapeNQRW = None
		self.scrapeBDFM = None
		self.scrapeL = None
		self.scrapeG = None
	
	def urlscrape(self):
		threading.Timer(15.0, urlscrape).start()
		
		self.scrape123456 = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=1')
		self.scrapeACE = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=26')
		self.scrapeNQRW = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=16')
		self.scrapeBDFM = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=21')
		self.scrapeL = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=2')
		self.scrapeG = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=31')
	

	def trainapp(self, trainchoice, stopchoice, updown):
		#define vars for each MTA get request 
		scrape123456 = self.scrape123456
		scrapeACE = self.scrapeACE
		scrapeBDFM = self.scrapeBDFM
		scrapeL = self.scrapeL
		scrapeG = self.scrapeG
	
		#inputs from form (views.py)
		trainchoice = str(trainchoice)
		stopchoice = str(stopchoice)+str(updown)
		
		#determine which feed to parse
		feed = gtfs_realtime_pb2.FeedMessage()
		if trainchoice == '6' or trainChoice == '4'or trainChoice == '5' or trainChoice == '1' or trainChoice == '2' or trainChoice == '3':
			feed.ParseFromString(scrape123456.content)

		elif trainchoice == 'A' or trainChoice == 'C' or trainChoice == 'E':
			feed.ParseFromString(scrapeACE.content)

		elif trainchoice == 'N' or trainChoice == 'Q' or trainChoice == 'R' or trainChoice == 'W':
			feed.ParseFromString(scrapeNQRW.content)

		elif trainchoice == 'B' or trainChoice == 'D' or trainChoice == 'F' or trainChoice == 'M':
			feed.ParseFromString(scrapeBDFM.content)

		elif trainchoice == 'L':
			feed.ParseFromString(scrapeL.content)

		elif trainchoice == 'G':
			feed.ParseFromString(scrapeG.content)
		arrivalTimeList = []
	
		for entity in feed.entity:
			if entity.HasField('trip_update') and entity.trip_update.trip.route_id == trainchoice:
				#print(entity.trip_update.stop_time_update)
				for stopTimeUpdate in entity.trip_update.stop_time_update:
					if stopTimeUpdate.stop_id == stopchoice:
						arrivalTimeList.append(stopTimeUpdate.arrival)
		
		#Calculate current time of day
		currTimeINT = int(datetime.datetime.utcnow().timestamp())
		currTimeSTR = datetime.datetime.fromtimestamp(int(currTimeINT)).strftime('%Y-%m-%d %H:%M:%S')
		
		#Create list of timestamps as integers and sort
		arrivalTimeList2 = []
		arrivalTimeList2.clear()
		
		for arrival in arrivalTimeList:
			x = str(arrival)
			x = x[-11:]
			x = int(x)
			arrivalTimeList2.append(x)       
		arrivalTimeList2.sort()
		
		#remove inaccurate data feed times
		if arrivalTimeList2[0] < currTimeINT:
			time1 = arrivalTimeList2[1]
			time2 = arrivalTimeList2[2]  
		else: 
			time1 = arrivalTimeList2[0]
			time2 = arrivalTimeList2[1]

		#Nearest Train Remaining Time UTC
		time1STR = datetime.datetime.utcfromtimestamp(time1)
		time1 = int(datetime.datetime.utcfromtimestamp(time1).timestamp())

		time1remain = (int(str(time1))-int(currTimeINT))/60
		time1remain = str(int(round(time1remain)))

		#Second Train Remaining Time UTC
		time2STR = datetime.datetime.utcfromtimestamp(time2)
		time2 = int(datetime.datetime.utcfromtimestamp(time2).timestamp())

		time2remain = (int(str(time2))-int(currTimeINT))/60
		time2remain = str(int(round(time2remain)))

		#print("The " + trainChoice + " train will arrive in " + str(time1remain) + " minutes")
		#print("The next " + trainChoice + " train will arrive in " +str(time2remain) + " minutes")
		return 'The next '+trainchoice+' train will arrive at '+stopchoice+' in '+time1remain+' minutes'
		
"""
		
def MTAscrapeLocal(trainchoice):
	#threading.Timer(15.0, MTAscrape).start()
	feed = gtfs_realtime_pb2.FeedMessage()
	
	if trainchoice == '6' or trainchoice == '4'or trainchoice == '5' or trainchoice == '1' or trainchoice == '2' or trainchoice == '3':
		#response = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=1')
		response = MTAscrape.response123456

	elif trainchoice == 'A' or trainchoice == 'C' or trainchoice == 'E':
		#response = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=26')
		response = MTAscrape.responseACE

	elif trainchoice == 'N' or trainchoice == 'Q' or trainchoice == 'R' or trainchoice == 'W':
		#response = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=16')
		response = MTAscrape.responseNQRW

	elif trainchoice == 'B' or trainchoice == 'D' or trainchoice == 'F' or trainchoice == 'M':
		#response = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=21')
		response = MTAscrape.responseBDFM

	elif trainchoice == 'L':
		#response = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=2')
		response = MTAscrape.responseL

	elif trainchoice == 'G':
		#response = requests.get('http://datamine.mta.info/mta_esi.php?key=152d23e8abffd5a2ab7751e03993092b&feed_id=31')
		response = MTAscrape.responseG
	
	feed.ParseFromString(response.content)
	
	return feed

def trainappDowntown(trainchoice, stopchoice, stopname):
	trainchoice = str(trainchoice)
	stopchoice = str(stopchoice)+'S'
	
	#trainchoice2 = int(trainchoice)
	#trainchoice2 += 1
	feed = MTAscrapeLocal(trainchoice)
	
	arrivalTimeList = []
	
	for entity in feed.entity:
		if entity.HasField('trip_update') and entity.trip_update.trip.route_id == trainchoice:
            #print(entity.trip_update.stop_time_update)
			for stopTimeUpdate in entity.trip_update.stop_time_update:
				if stopTimeUpdate.stop_id == stopchoice:
					arrivalTimeList.append(stopTimeUpdate.arrival)
	
	#Calculate current time of day
	currTimeINT = int(datetime.datetime.utcnow().timestamp())
	currTimeSTR = datetime.datetime.fromtimestamp(int(currTimeINT)).strftime('%Y-%m-%d %H:%M:%S')
    
    #Create list of timestamps as integers and sort
	arrivalTimeList2 = []
	arrivalTimeList2.clear()
    
	for arrival in arrivalTimeList:
		x = str(arrival)
		x = x[-11:]
		x = int(x)
		arrivalTimeList2.append(x)       
	arrivalTimeList2.sort()
    
    #remove inaccurate data feed times
	if arrivalTimeList2[0] < currTimeINT:
		time1 = arrivalTimeList2[1]
		time2 = arrivalTimeList2[2]  
	else: 
		time1 = arrivalTimeList2[0]
		time2 = arrivalTimeList2[1]

    #Nearest Train Remaining Time UTC
	time1STR = datetime.datetime.utcfromtimestamp(time1)
	time1 = int(datetime.datetime.utcfromtimestamp(time1).timestamp())

	time1remain = (int(str(time1))-int(currTimeINT))/60
	time1remain = str(int(round(time1remain)))

    #Second Train Remaining Time UTC
	time2STR = datetime.datetime.utcfromtimestamp(time2)
	time2 = int(datetime.datetime.utcfromtimestamp(time2).timestamp())

	time2remain = (int(str(time2))-int(currTimeINT))/60
	time2remain = str(int(round(time2remain)))
	
	#downtown1 = 'The next Downtown '+trainchoice+' train will arrive at '+stopname+' in '+time1remain+' minute(s)'
	#downtown2 = 'The following Downtown '+trainchoice+' train will arrive at '+stopname+' in '+time2remain+' minute(s)'
	downtown1 = 'Downtown '+time1remain+' min'
	downtown2 = 'Downtown '+time2remain+' min'
	
	return downtown1, downtown2
	

def trainappUptown(trainchoice, stopchoice, stopname): #updown
	trainchoice = str(trainchoice)
	stopchoice = str(stopchoice)+'N'
	
	#trainchoice2 = int(trainchoice)
	#trainchoice2 += 1
	feed = MTAscrapeLocal(trainchoice)
	
	arrivalTimeList = []
	
	for entity in feed.entity:
		if entity.HasField('trip_update') and entity.trip_update.trip.route_id == trainchoice:
            #print(entity.trip_update.stop_time_update)
			for stopTimeUpdate in entity.trip_update.stop_time_update:
				if stopTimeUpdate.stop_id == stopchoice:
					arrivalTimeList.append(stopTimeUpdate.arrival)
	
	#Calculate current time of day
	currTimeINT = int(datetime.datetime.utcnow().timestamp())
	currTimeSTR = datetime.datetime.fromtimestamp(int(currTimeINT)).strftime('%Y-%m-%d %H:%M:%S')
    
    #Create list of timestamps as integers and sort
	arrivalTimeList2 = []
	arrivalTimeList2.clear()
    
	for arrival in arrivalTimeList:
		x = str(arrival)
		x = x[-11:]
		x = int(x)
		arrivalTimeList2.append(x)       
	arrivalTimeList2.sort()
    
    #remove inaccurate data feed times
	if arrivalTimeList2[0] < currTimeINT:
		time1 = arrivalTimeList2[1]
		time2 = arrivalTimeList2[2]  
	else: 
		time1 = arrivalTimeList2[0]
		time2 = arrivalTimeList2[1]

    #Nearest Train Remaining Time UTC
	time1STR = datetime.datetime.utcfromtimestamp(time1)
	time1 = int(datetime.datetime.utcfromtimestamp(time1).timestamp())

	time1remain = (int(str(time1))-int(currTimeINT))/60
	time1remain = str(int(round(time1remain)))

    #Second Train Remaining Time UTC
	time2STR = datetime.datetime.utcfromtimestamp(time2)
	time2 = int(datetime.datetime.utcfromtimestamp(time2).timestamp())

	time2remain = (int(str(time2))-int(currTimeINT))/60
	time2remain = str(int(round(time2remain)))

	#uptown1 = 'The next Uptown '+trainchoice+' train will arrive at '+stopname+' in '+time1remain+' minute(s)'
	#uptown2 = 'The following Uptown '+trainchoice+' train will arrive at '+stopname+' in '+time2remain+' minute(s)'
	
	uptown1 = 'Uptown '+time1remain+' min'
	uptown2 = 'Uptown '+time2remain+' min'
	
	return uptown1, uptown2

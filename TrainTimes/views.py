from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import JsonResponse
from TrainTimes.models import train
from TrainTimes.forms import TrainChoice
from TrainTimes.trainapp import trainappDowntown, trainappUptown
from TrainTimes.MTAscrape import response123456
from google.transit import gtfs_realtime_pb2
import json


# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)
		
class AboutPageView(TemplateView):
	template_name = "about.html"
	
def detail(request, train_id):
	html=''
	#all_trains = 	
	
	return HttpResponse('<h2>Details for Train Selection '+str(train_id)+'</h2>')
	#return HttpResponse(html)


def ChoicePage(request):
	#If this is a POST request we need to proess the form data
	if request.method == 'POST':
		#create a form instance and populate it with data from the request
		form = TrainChoice(request.POST)
		if form.is_valid():
			#process the data is form.cleaned_data as required
			trainchoice = form.cleaned_data['train_choice']
			stopname = form.cleaned_data['stop_choice']
			#updown = form.cleaned_data['UpDown']
			#if updown == 'Downtown' or updown == 'downtown':
				#updown = 'S'
			#else:
				#updown = 'N'
				
			#Concatenate and retrieve stop_id
			trainstop = str(trainchoice)+" "+str(stopname)
			stopchoice = train.objects.filter(stop_key__contains = trainstop).values_list('stop_id', flat=True).distinct()
			stopchoicedict=[]
			for stop in stopchoice:
				stopchoicedict.append(stop)
			stopchoice = stopchoicedict[0]
			
			#trainchoice2 = MTAscrape()
			
			traintimestitle = str(trainchoice)+' train at '+str(stopname)
			traintimesDown = trainappDowntown(trainchoice=trainchoice, stopchoice=stopchoice, stopname=stopname) #updown=updown
			traintimesUp = trainappUptown(trainchoice=trainchoice, stopchoice=stopchoice, stopname=stopname)#updown=updown
			#return HttpResponseRedirect('return/')
			
		args = {'form': form, 'downtown1':traintimesDown[0], 'downtown2':traintimesDown[1], 'uptown1':traintimesUp[0], 'uptown2':traintimesUp[1], 'traintimestitle':traintimestitle}
		return render(request, 'trainchoice.html', args)
		#return render('ajaxStop.html', {'validStops' : validStops})
		
	else:
		form = TrainChoice()
		
	return render(request, 'trainchoice.html', {'form':form})
"""
Try to create a view specific to a url that simply returns a JsonResponse file saved by an ever-running application
	
"""

def SearchStop(request):
	if request.method == 'POST':
		formStop = request.POST['SearchStop']
		formTrain = request.POST['SearchTrain']
	else:
		formStop = ''
	
	validStop = train.objects.filter(stop_name__icontains=formStop).filter(train_name__iexact=formTrain).values_list('stop_name', flat=True).order_by('stop_name').distinct()
	#response = JsonResponse(dict(list(validStop)))
		
	stopList=[]
	
	if validStop.count() > 0:
		for stop in validStop:
			stopList.append(stop)
	else:
		stopList.append("No Matching Stops")
	
	return JsonResponse(stopList, safe=False)
	
def Response123456(request):
	responseData = gtfs_realtime_pb2.FeedMessage()
	response = response123456
	responseData.ParseFromString(response.content)
	responseData = str(responseData)
	return JsonResponse(responseData, safe = False)
	
